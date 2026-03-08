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
- `README.md`: guia de uso del proyecto

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

## Notas

- La rama `main` se mantiene enfocada en el lenguaje MICELIO funcional.
- El tooling/editor (sintaxis de VS Code) vive en la rama `tooling/vscode-syntax`.
