# LinearSolver

Proyecto en Python para resolver sistemas de ecuaciones lineales de la forma
**Ax = b**, con una arquitectura separada para validación, eliminación gaussiana,
sustitución y resultados.

## Estado del proyecto

La estructura inicial, los tipos compartidos, la jerarquía de excepciones y la
configuración están preparados. Los algoritmos, la API pública, la representación
de resultados y las pruebas aún están pendientes de implementación.

## Requisitos e instalación

Se requiere Python 3.11 o superior. El paquete base no declara dependencias
externas.

Desde la carpeta del proyecto, en PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

Si ya existe un entorno virtual, utiliza directamente el segundo comando.

## Organización

```text
src/linearsolver/
├── __init__.py
├── types.py            # Tipos de entrada y estructuras mutables internas
├── exceptions.py       # Errores propios de la biblioteca
├── core/
│   ├── __init__.py
│   ├── validation.py   # Validación de dimensiones y valores (pendiente)
│   ├── elimination.py  # Eliminación gaussiana (pendiente)
│   └── substitution.py # Sustitución (pendiente)
├── solvers/
│   ├── __init__.py
│   └── gaussian.py     # Coordinación del método gaussiano (pendiente)
└── results.py          # Representación de resultados (pendiente)
tests/                  # Pruebas
benchmarks/             # Mediciones de rendimiento
examples/               # Ejemplos de uso
```

## Tipos compartidos

- `Scalar`: un coeficiente real representado mediante `int` o `float`.
- `Vector`: una secuencia de coeficientes.
- `Matrix`: una secuencia de filas, cada una con sus coeficientes.
- `MutableVector` y `MutableMatrix`: listas de valores `float` para los cálculos.

Estos tipos expresan contratos de anotación; no validan datos en ejecución.
Los algoritmos deberán copiar las entradas antes de modificarlas.

```python
from linearsolver.types import Matrix, Vector

a: Matrix = [[2, 1], [1, -1]]
b: Vector = [5, 1]
```

El ejemplo solo define las entradas: todavía no existe un solucionador funcional.

## Excepciones

```text
LinearSolverError
├── ValidationError (también ValueError)
│   └── DimensionError
└── NumericalError (también ArithmeticError)
    └── SingularMatrixError
        ├── InconsistentSystemError
        └── InfiniteSolutionsError
```

Una matriz singular no admite solución única. Las excepciones específicas
permiten distinguir un sistema sin solución de uno con infinitas soluciones
cuando el algoritmo detecte esas situaciones.

## Desarrollo

```powershell
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
```

Por ahora, `tests/` está vacío: pytest informará que no hay pruebas y devolverá
el código de salida 5. Añade pruebas al implementar los módulos.
