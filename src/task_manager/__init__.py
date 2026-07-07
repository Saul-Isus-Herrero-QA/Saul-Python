"""Task Manager"""

__version__ = "2.1.0"
__author__ = "Saul"
__description__ = "Sistema de gestión de tareas con SOLID y Clean Code"

from .ai_engine import AIEngine
from .cli import CLIApplication
from .exceptions import (
    EmptyTaskDescriptionError,
    InvalidTaskIndexError,
    TaskManagerException,
)
from .models import TaskManager

__all__ = [
    "TaskManager",
    "CLIApplication",
    "AIEngine",
    "TaskManagerException",
    "InvalidTaskIndexError",
    "EmptyTaskDescriptionError",
]
