# Auditoria de rendimiento

Fecha: 2026-03-09
Proyecto: Micelio (ANTLR4 + Python)

## Objetivo

Documentar:

- Cual era el problema de rendimiento antes de optimizar.
- Como se diagnostico.
- Que cambios se aplicaron.
- Que resultados se observaron en pruebas reales.
- Que limites persisten por arquitectura.

## Contexto del problema

Al comparar bucles entre Micelio, Python y C++, Micelio resultaba mucho mas lento.

El caso inicial tambien mezclaba dos factores que distorsionaban el analisis:

1. Impresion en pantalla dentro del bucle (`imp`), que agrega costo de I/O en cada iteracion.
2. Limites extremadamente altos (hasta `10^21`), inviables en tiempo real para cualquier runtime.

Luego de normalizar pruebas, se confirmo que el cuello principal era overhead del interprete (visitor + dispatch + scopes), no solo I/O.

## Diagnostico y aproximacion

Se siguio un enfoque incremental:

1. Separar pruebas de CPU vs pruebas con I/O.
2. Medir en escenarios pequenos y luego grandes (hasta 1,000,000 iteraciones).
3. Perfilar con `cProfile` para evitar optimizaciones "a ciegas".
4. Optimizar hot-path sin cambiar arquitectura base (seguir en ANTLR + Python).

Hallazgos del perfilado:

- Alto tiempo acumulado en dispatch generico del visitor (`visitChildren` de ANTLR).
- Alto costo por iteracion en `visitBlock` por creacion de `Environment` repetida.
- Costo recurrente en lookups/asignaciones de variables por scope chain.

## Estado antes de optimizaciones

Caracteristicas observadas:

- `Environment.get/assign` con recursion en cadena de scopes.
- Asignaciones en algunos caminos usando excepciones como control de flujo normal.
- `visitStatement` delegando a `visitChildren` en muchos casos.
- `while/for` reevaluando accesos de contexto sin cache local en cada vuelta.
- En bucles, creacion de scope para bloques aunque el cuerpo no declarara simbolos.

## Cambios aplicados

### 1) Runtime: acceso y asignacion de variables

Archivo: `MICELIO/runtime.py`

- `Environment.get` paso de recursion a traversal iterativo.
- `Environment.assign` paso de recursion a traversal iterativo.

Impacto esperado:

- Menos llamadas Python por lookup.
- Menor overhead en scopes profundos o bucles intensivos.

### 2) Visitor: asignacion sin excepcion en flujo normal

Archivo: `MICELIO/eval_visitor.py`

- `_assign_or_define` ahora resuelve entorno destino y asigna directo.
- Se evita `try/except` para casos normales de asignacion.

Impacto esperado:

- Menos costo por iteracion en rutas frecuentes de escritura.

### 3) Visitor: dispatch explicito para sentencias

Archivo: `MICELIO/eval_visitor.py`

- `visitStatement` con ruta explicita a `simple_stmt` y `compound_stmt`.
- Nuevos `visitSimple_stmt` y `visitCompound_stmt` con dispatch directo.
- Menor dependencia de `visitChildren` en camino caliente.

Impacto esperado:

- Reduccion del overhead de despacho dinamico del arbol ANTLR.

### 4) Bucles: cache y fast-path

Archivo: `MICELIO/eval_visitor.py`

- Cache local de `ctx.block()`/`ctx.expr()` en `while` y `for`.
- En `for`, resolucion previa del entorno donde vive la variable de control.
- Fast-path para ejecutar cuerpo de bloque sin crear scope por iteracion cuando no hay declaraciones (`var/const/funcion/importar/leer`).

Impacto esperado:

- Menos allocations de `Environment` por vuelta.
- Menos overhead de contexto dentro del loop.

### 5) Benchmark reproducible

Archivo: `MICELIO/bench_print_loops.py`

- Compara Micelio vs Python en:
  - `for` numerico
  - `while`
  - `for en lista`
- Pruebas con impresion real en pantalla (`imp/print`) y resumen de tiempos.

## Resultados observados

### Prueba grande con salida en terminal (progreso cada 100k)

Escenario: 1,000,000 iteraciones, `imp/print` por checkpoint.

Valores observados:

- Micelio `for`: ~29.4s en medicion base y ~27.5-27.9s en corridas posteriores.
- Python `for`: ~0.10s.
- Micelio `while`: ~48.9s (medicion registrada).
- Python `while`: ~0.15s.

Lectura correcta:

- Si hubo mejora incremental en Micelio tras optimizaciones de hot-path.
- La brecha grande persiste por diferencia estructural (ver seccion de limites).

## Por que sigue habiendo brecha grande

Aunque se optimizo, Micelio sigue siendo:

1. Un interprete AST/visitor en Python.
2. Con dispatch por nodo del parse tree.
3. Con semantica dinamica y chequeos en tiempo de ejecucion.

Python ya ejecuta su bytecode con una VM altamente optimizada en C. Por eso, aun con mejoras, no es esperable igualar Python nativo en loops puros.

## Diferencias de aproximacion (antes vs despues)

Antes:

- Ajustes puntuales sin perfilado continuo.
- Alto costo oculto en dispatch y scope churn.

Despues:

- Enfoque guiado por medicion (`benchmark` + `cProfile`).
- Optimizaciones en rutas calientes reales.
- Cambios conservadores para mantener compatibilidad y semantica del lenguaje.

## Riesgos y notas

- Fast-path sin scope nuevo en bucles se aplica solo cuando el bloque no declara simbolos. Esto reduce riesgo semantico.
- Microbenchmarks pequenos pueden tener ruido por calentamiento del proceso.
- Pruebas con mucha salida pueden medir mas I/O que CPU del interprete.

## Recomendaciones siguientes

1. Agregar modo benchmark oficial (`--bench`) con split parse/execute.
2. Introducir cache de parse tree por archivo para ejecuciones repetidas.
3. Explorar una capa intermedia de IR/bytecode (manteniendo ANTLR y Python) para reducir llamadas por nodo.
4. Mantener un set fijo de benchmarks de regresion de rendimiento por release.

## Conclusiones

- El problema original fue real y medible.
- Se aplicaron optimizaciones concretas y seguras en hot-path.
- Se obtuvieron mejoras incrementales sin abandonar ANTLR + Python.
- Para saltos grandes de rendimiento, el siguiente paso natural es reducir la granularidad de ejecucion por nodo (IR/bytecode), no solo microajustes.
