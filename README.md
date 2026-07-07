# Task Manager - Sistema Profesional de Gestión de Tareas

> Una aplicación de consola moderna y profesional para gestionar listas de tareas (To-Do List) en Python, construida siguiendo principios **SOLID** y **Clean Code**.

## 📋 Descripción

Task Manager es un gestor de tareas de línea de comandos desarrollado con arquitectura limpia, logging centralizado, manejo robusto de errores y una suite completa de tests unitarios.

## 🎯 Características

- ✅ **Arquitectura Limpia**: Separación clara de responsabilidades con SOLID
- ✅ **Logging Profesional**: Sistema de logging con rotación de archivos
- ✅ **Tests Unitarios**: Suite completa de tests con pytest y cobertura
- ✅ **Type Hints**: Tipado completo de Python para mejor mantenibilidad
- ✅ **Manejo de Errores**: Excepciones personalizadas y tratamiento robusto
- ✅ **Inyección de Dependencias**: Patrón DI implementado correctamente
- ✅ **Documentación**: Docstrings exhaustivos en formato Google/NumPy
- ✅ **Validación de Entrada**: Validación completa de datos
- ✅ **Interfaz Amigable**: CLI con emojis y mensajes claros

## 📦 Stack Tecnológico

### Core
- **Lenguaje**: Python 3.9+
- **Editor**: Visual Studio Code
- **SO**: Windows/macOS/Linux

### Desarrollo
- **Testing**: pytest 7.4.3
- **Cobertura**: pytest-cov 4.1.0
- **Linting**: flake8 6.1.0
- **Formateo**: black 23.12.1
- **Type Checking**: mypy 1.8.0
- **Pre-commit**: pre-commit 3.6.0

## 📂 Estructura del Proyecto

```
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

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone <repository-url>
cd Saul-Python
```

### 2. Crear entorno virtual
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. (Opcional) Instalar pre-commit hooks
```bash
pre-commit install
```

## 📖 Uso

### Ejecutar la aplicación
```bash
python main.py
```

### Menú de opciones
```
¿Qué deseas hacer?
1️⃣  Agregar tarea
2️⃣  Eliminar tarea
3️⃣  Listar tareas
4️⃣  Salir
```

### Ejemplo interactivo
```
✏️  Escribe una tarea para tu lista: Estudiar Python
✅ ¡Tarea agregada con éxito!

3️⃣  Listar tareas
1. Estudiar Python
Total: 1 tarea(s)
```

## 🧪 Testing

### Ejecutar todos los tests
```bash
pytest
```

### Ejecutar tests con cobertura
```bash
pytest --cov=src/task_manager --cov-report=html
```

### Ver reporte HTML de cobertura
```bash
# En Windows
start htmlcov/index.html
# En macOS
open htmlcov/index.html
# En Linux
firefox htmlcov/index.html
```

### Ejecutar tests con output verbose
```bash
pytest -v
```

## 🔍 Linting y Formateo

### Verificar código con Black
```bash
black --check src/ tests/
```

### Formatear código automáticamente
```bash
black src/ tests/ main.py
```

### Verificar con flake8
```bash
flake8 src/ tests/ main.py
```

### Type checking con mypy
```bash
mypy src/ main.py
```

### Ordenar imports con isort
```bash
isort src/ tests/ main.py
```

## 📝 API de TaskManager

### TaskManager
```python
from src.task_manager import TaskManager

# Crear instancia
manager = TaskManager()

# Agregar tarea
manager.add("Estudiar Python")  # Returns: True

# Obtener todas las tareas
manager.get_all()  # Returns: ['Estudiar Python']

# Eliminar tarea
manager.delete(0)  # Returns: 'Estudiar Python'

# Verificar si está vacío
manager.is_empty()  # Returns: True

# Contar tareas
manager.count()  # Returns: 0
```

### CLIApplication
```python
from src.task_manager import TaskManager, CLIApplication

manager = TaskManager()
app = CLIApplication(manager=manager)

# Ejecutar interfaz interactiva
app.run()

# O métodos individuales
app.list_tasks()
app.handle_add()
app.handle_delete()
```

## 📊 Cobertura de Tests

Objetivo: **>95%** de cobertura de código

Áreas cubiertas:
- ✅ TaskManager.add() - validación y casos límite
- ✅ TaskManager.delete() - índices válidos e inválidos
- ✅ TaskManager.get_all() - retorna copia
- ✅ Manejo de excepciones personalizadas
- ✅ Type checking y validación de entrada

## 🛠️ Desarrollo

### Agregar nueva funcionalidad

1. **Escribir test primero** (TDD)
   ```bash
   # En tests/test_task_manager.py
   def test_nueva_funcionalidad():
       ...
   ```

2. **Implementar funcionalidad**
   ```bash
   # En src/task_manager/models.py o cli.py
   ```

3. **Verificar tests pasan**
   ```bash
   pytest
   ```

4. **Validar linting**
   ```bash
   black src/
   flake8 src/
   mypy src/
   ```

5. **Commit con pre-commit hooks**
   ```bash
   git add .
   git commit -m "feat: nueva funcionalidad"
   ```

## 📋 Principios SOLID Implementados

- **S**ingle Responsibility: Cada clase tiene una única razón de cambio
- **O**pen/Closed: Abierto para extensión, cerrado para modificación
- **L**iskov Substitution: Las excepciones heredan de base común
- **I**nterface Segregation: Interfaces limpias y específicas
- **D**ependency Inversion: Inyección de dependencias en CLIApplication

## 🎓 Clean Code Principles

- ✅ Nombres descriptivos y significativos
- ✅ Funciones pequeñas y enfocadas
- ✅ DRY (Don't Repeat Yourself)
- ✅ KISS (Keep It Simple, Stupid)
- ✅ Comentarios significativos
- ✅ Manejo de errores explícito
- ✅ Logging exhaustivo

## 📜 Versionado

Siguiendo [Semantic Versioning](https://semver.org/):
- **MAJOR**: Cambios incompatibles en la API
- **MINOR**: Nuevas funcionalidades compatibles
- **PATCH**: Correcciones de bugs

Versión actual: `2.1.0`

## 👤 Autor

**Saul**
- GitHub: https://github.com/Saul-Isus-Herrero-QA/
- Email: saul.isus.herrero@gmail.com

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📞 Soporte

Para reportar bugs o sugerir mejoras, abre un issue en el repositorio.

## 🔄 Roadmap

- [ ] Persistencia con SQLite
- [ ] Exportar tareas a JSON/CSV
- [ ] Categorías y etiquetas para tareas
- [ ] Fechas de vencimiento
- [ ] API REST con FastAPI
- [ ] Interfaz web con React
- [ ] Sincronización en la nube

---

**Stack:** Python 3.9+
