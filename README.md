# MICELIO

Lenguaje de programacion interpretado basado en ANTLR + Python, con enfoque didactico y soporte funcional.

## Estado actual

Incluye:

- Gramatica ANTLR del lenguaje (`MICELIO/Micelio.g4`)
- Lexer/Parser/Visitor generados
- Interprete por visitor (`MICELIO/eval_visitor.py`)
- Runtime con entorno, funciones, control de flujo y builtins (`MICELIO/runtime.py`)
- Importacion de modulos `.mice` desde archivos
- Modulos estandar en `MICELIO/modulos_std/` (actualmente `math.mice`)

## Estructura principal

- `MICELIO/`: implementacion del lenguaje
- `MICELIO/modulos_std/`: modulos del lenguaje en archivos `.mice`
- `micelio-vscode/`: extension de sintaxis para VS Code
- `main.tex`: especificacion tecnica del lenguaje
- `Pruebas/`: carpeta historica de pruebas

## Requisitos

- Python 3.10+
- `antlr4-python3-runtime`

Instalacion rapida:

```bash
pip install antlr4-python3-runtime
```

## Ejecutar programas Micelio

Desde la carpeta `MICELIO`:

```bash
python3 main.py archivo.mice
```

Ejemplo:

```bash
cd MICELIO
python3 main.py A.mice
```

## Modulos estandar

Los modulos del lenguaje se colocan en:

- `MICELIO/modulos_std/`

Importacion (ejemplo):

```mice
importar "math.mice" como math
imp math.seno(math.PI / 2)
```

### Modulo Math (`MICELIO/modulos_std/math.mice`)

Funciones incluidas:

- `PI`, `E`
- `seno`, `coseno`, `tangente`
- `arcoseno`, `arcocoseno`, `arcotangente`
- `raiz`, `log`, `log10`, `exp`, `potencia`
- `abs`, `piso`, `techo`, `redondear`

## Utilidades de texto en Micelio

Metodo disponible en strings:

- `texto.separar()`
- `texto.separar(separador)`

Tambien existe alias:

- `texto.split(...)`

## Sintaxis de Micelio en VS Code

Se creo una extension local para coloreado de sintaxis:

- Carpeta: `micelio-vscode/`
- Paquete VSIX: `micelio-vscode/micelio-syntax-0.0.1.vsix`

### Instalar la sintaxis

Opcion 1: instalacion directa del `.vsix`

```bash
code --install-extension micelio-vscode/micelio-syntax-0.0.1.vsix --force
```

Opcion 2: instalar desde release de GitHub

- Release: `Micelio Syntax v0.0.1`
- Descarga el `.vsix` y ejecuta:

```bash
code --install-extension micelio-syntax-0.0.1.vsix --force
```

### Asociacion de archivos

Ya incluida en `.vscode/settings.json`:

- `*.mice` -> `micelio`
- `*.micelio` -> `micelio`

## Notas

- Este repositorio prioriza el desarrollo del lenguaje (`MICELIO`) sobre tooling adicional.
- La extension de VS Code esta en estado "minimo util" para mejorar ergonomia de desarrollo.
