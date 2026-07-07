# Contribuyendo a Task Manager

¡Gracias por tu interés en contribuir! Este documento te guía en el proceso.

## Código de Conducta

Este proyecto y todos sus participantes se rigen por nuestro [Código de Conducta](CODE_OF_CONDUCT.md). Al participar, se espera que mantengas este código.

## ¿Cómo contribuir?

### Reportar Bugs

Antes de crear un reporte de bug, verifica si ya existe. Si encuentras un bug:

1. **Usa un título claro y descriptivo**
2. **Describe los pasos exactos para reproducirlo**
3. **Proporciona ejemplos específicos**
4. **Describe el comportamiento observado**
5. **Describe el comportamiento esperado**
6. **Incluye capturas o logs si es relevante**

### Sugerir Mejoras

Las sugerencias son bienvenidas. Al crear una sugerencia:

1. **Usa un título claro y descriptivo**
2. **Proporciona una descripción detallada**
3. **Incluye ejemplos de código si es relevante**
4. **Explica por qué esta mejora sería útil**

### Pull Requests

- Sigue el estilo de código del proyecto
- Incluye tests apropiados
- Actualiza la documentación según sea necesario
- Termina todos los archivos con una nueva línea

## Guía de Desarrollo

### Setup

```bash
git clone <repository>
cd Saul-Python
python -m venv venv
source venv/bin/activate  # o `venv\\Scripts\\activate` en Windows
pip install -r requirements.txt
pre-commit install
```

### Flujo de trabajo

1. **Crea una rama**
   ```bash
   git checkout -b feature/tu-feature
   ```

2. **Escribe tests primero** (TDD)
   ```bash
   # En tests/test_task_manager.py
   def test_tu_funcionalidad():
       # Test aquí
   ```

3. **Implementa tu funcionalidad**

4. **Ejecuta tests y linting**
   ```bash
   pytest                    # Tests
   black src/ tests/ main.py # Formateo
   flake8 src/ tests/        # Linting
   mypy src/                 # Type checking
   ```

5. **Commit**
   ```bash
   git add .
   git commit -m "feat: descripción breve"
   ```

6. **Push y abre PR**
   ```bash
   git push origin feature/tu-feature
   ```

## Estándares de Código

### Estilo

- Seguimos **PEP 8** y **PEP 257**
- Usamos **Black** para formateo automático
- Línea máxima: 99 caracteres
- Indentación: 4 espacios

### Type Hints

Todos los parámetros y retornos deben estar tipados:

```python
def add_task(description: str) -> bool:
    """
    Agrega una tarea.
    
    Args:
        description: Descripción de la tarea.
        
    Returns:
        bool: True si se agregó con éxito.
    """
```

### Docstrings

Usamos formato Google:

```python
def funcion(param1: str, param2: int) -> bool:
    """
    Descripción breve de una línea.
    
    Descripción más larga si es necesario.
    
    Args:
        param1: Descripción del primer parámetro.
        param2: Descripción del segundo parámetro.
        
    Returns:
        bool: Descripción del retorno.
        
    Raises:
        ValueError: Si param1 está vacío.
        
    Example:
        >>> resultado = funcion("test", 42)
        >>> resultado
        True
    """
```

### Excepciones

Crea excepciones personalizadas heredando de `TaskManagerException`:

```python
class MiExcepcion(TaskManagerException):
    """Descripción clara de la excepción."""
    pass
```

## Estructura de Tests

```python
class TestMiClase:
    """Suite de tests para MiClase."""
    
    @pytest.fixture
    def instancia(self) -> MiClase:
        """Fixture que proporciona instancia."""
        return MiClase()
    
    def test_caso_1(self, instancia: MiClase) -> None:
        """Test: descripción del caso."""
        # Arrange
        # Act
        # Assert
```

## Mensajes de Commit

Sigue [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Tipos: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Ejemplos:**
```
feat: agregar soporte para categorías
fix: corregir bug en eliminación de tareas
docs: actualizar guía de instalación
test: agregar tests para nueva funcionalidad
```

## Proceso de Review

1. Mínimo 2 aprobaciones requeridas
2. CI/CD debe pasar
3. Cobertura no debe disminuir
4. Documentación debe estar actualizada

## Preguntas

¿Tienes preguntas? Abre una issue con la etiqueta `question`.

---

¡Gracias por contribuir! 🎉
