## Context
Proyecto enfocado en aplicar las mejores prácticas de programación: SOLID y Clean Code en Python.

## Objetivos

### Primarios
1. Construir una aplicación de consola profesional para gestionar listas de tareas
2. Implementar principios SOLID completamente
3. Seguir estándares de Clean Code

### Secundarios
1. Establecer estructura de proyecto escalable y mantenible
2. Crear suite completa de tests unitarios
3. Implementar logging centralizado
4. Usar type hints exhaustivos
5. Automatizar linting y formateo con pre-commit

## Stack Técnico

### Core
- **Lenguaje:** Python 3.9+
- **Editor:** Visual Studio Code
- **Sistema Operativo:** Windows (PATH configuration)

### Testing & Quality
- **Testing:** pytest 7.4.3, pytest-cov 4.1.0
- **Linting:** flake8 6.1.0, pylint 3.0.3
- **Formateo:** black 23.12.1, isort 5.13.2
- **Type Checking:** mypy 1.8.0
- **Pre-commit:** pre-commit 3.6.0

### Development
- **Build:** setuptools 68.0+, wheel
- **Logging:** logging (stdlib)
- **Documentation:** Docstrings Google format

## Principios Implementados

### SOLID
- **S**ingle Responsibility: TaskManager solo gestiona tareas; CLIApplication solo interfaz
- **O**pen/Closed: Extensible sin modificar código existente
- **L**iskov Substitution: Excepciones con jerarquía correcta
- **I**nterface Segregation: Métodos específicos y cohesivos
- **D**ependency Inversion: Inyección de dependencias en CLIApplication

### Clean Code
- ✅ Nombres significativos y autoexplicativos
- ✅ Funciones pequeñas y enfocadas (single responsibility)
- ✅ DRY - Don't Repeat Yourself
- ✅ KISS - Keep It Simple, Stupid
- ✅ Manejo explícito de errores
- ✅ Logging exhaustivo
- ✅ Type hints completos
- ✅ Docstrings detallados

## Estructura del Proyecto

```
src/task_manager/
  ├── __init__.py        # API pública
  ├── models.py          # Lógica de negocio
  ├── cli.py             # Interfaz de usuario
  └── exceptions.py      # Excepciones personalizadas

config/
  └── logging_config.py  # Configuración centralizada

tests/
  └── test_task_manager.py  # Suite de tests

main.py                  # Punto de entrada
```

## Estándares de Código

- **Línea máxima:** 99 caracteres
- **Indentación:** 4 espacios
- **Type hints:** Todos los parámetros y retornos
- **Docstrings:** Formato Google, exhaustivos
- **Cobertura de tests:** Objetivo >95%
- **Pre-commit:** Todos los hooks habilitados

## Recursos de Referencia

- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Clean Code by Robert C. Martin](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
- [PEP 8 - Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [PEP 257 - Docstrings](https://www.python.org/dev/peps/pep-0257/)
- [Type Hints in Python](https://docs.python.org/3/library/typing.html)

## Versión Actual
2.1.0 (Semantic Versioning)
