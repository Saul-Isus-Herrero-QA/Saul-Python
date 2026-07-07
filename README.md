## Descripción
Task Manager es un gestor de tareas de línea de comandos desarrollado con arquitectura limpia, logging centralizado, manejo robusto de errores y una suite completa de tests unitarios.

## Stack
**Lenguaje**: Python 3.9+
**Editor**: Visual Studio Code

### Desarrollo
- **Testing**: pytest 7.4.3
- **Cobertura**: pytest-cov 4.1.0
- **Linting**: flake8 6.1.0
- **Formateo**: black 23.12.1
- **Type Checking**: mypy 1.8.0
- **Pre-commit**: pre-commit 3.6.0

## Estructura del Proyecto

Saul-Python/
├── src/
│   └── task_manager/           # Módulo principal
│       ├── __init__.py         # Exportaciones públicas
│       ├── models.py           # Lógica de negocio (TaskManager)
│       ├── cli.py              # Interfaz de usuario (CLIApplication)
│       └── exceptions.py       # Excepciones personalizadas
├── config/
│   └── logging_config.py       # Configuración centralizada de logging
├── tests/
│   ├── __init__.py
│   └── test_task_manager.py   # Suite de tests unitarios
├── logs/                       # Directorio para logs (generado en runtime)
├── main.py                     # Punto de entrada principal
├── pyproject.toml              # Configuración del proyecto (PEP 518)
├── requirements.txt            # Dependencias del proyecto
├── .gitignore                  # Configuración de git
├── .pre-commit-config.yaml     # Hooks pre-commit
├── README.md                   # Este archivo
└── AI.md                       # Documentación de contexto
```

## 👤 Autor

**Saul**
- GitHub: https://github.com/Saul-Isus-Herrero-QA/
- Email: saul.isus.herrero@gmail.com

