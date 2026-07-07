"""Definición de excepciones personalizadas para la aplicación."""


class TaskManagerException(Exception):
    """Excepción base para todos los errores de TaskManager."""

    pass


class InvalidTaskIndexError(TaskManagerException):
    """Se levanta cuando el índice de tarea es inválido."""

    pass


class EmptyTaskDescriptionError(TaskManagerException):
    """Se levanta cuando la descripción de tarea está vacía."""

    pass
