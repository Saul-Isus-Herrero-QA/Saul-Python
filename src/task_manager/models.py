"""Modelos de negocio para la gestión de tareas."""

import logging
from typing import List

from .exceptions import EmptyTaskDescriptionError, InvalidTaskIndexError

logger = logging.getLogger(__name__)


class TaskManager:
    """
    Gestor de tareas.

    Gestiona el ciclo de vida completo de tareas con validación,
    logging y manejo de errores.

    Attributes:
        _tasks: Lista interna de tareas como strings.
    """

    def __init__(self) -> None:
        """Inicializa el gestor de tareas con lista vacía."""
        self._tasks: List[str] = []
        logger.info("TaskManager inicializado")

    def get_all(self) -> List[str]:
        """
        Retorna una copia de la lista actual de tareas.

        Returns:
            List[str]: Copia de la lista de tareas.

        Example:
            >>> manager = TaskManager()
            >>> manager.add("Comprar leche")
            True
            >>> manager.get_all()
            ['Comprar leche']
        """
        logger.debug(f"get_all(): retornando {len(self._tasks)} tareas")
        return self._tasks.copy()

    def add(self, description: str) -> bool:
        """
        Valida y añade una nueva tarea al listado.

        Args:
            description: Descripción de la tarea (será trimmed).

        Returns:
            bool: True si se agregó con éxito, False si estaba vacía.

        Raises:
            TypeError: Si description no es string.

        Example:
            >>> manager = TaskManager()
            >>> manager.add("Estudiar Python")
            True
            >>> manager.add("   ")
            False
        """
        if not isinstance(description, str):
            logger.error(f"add(): tipo inválido: {type(description)}")
            raise TypeError("La descripción debe ser un string")

        cleaned_description = description.strip()

        if not cleaned_description:
            logger.warning("add(): intento de agregar tarea vacía")
            raise EmptyTaskDescriptionError(
                "La descripción de la tarea no puede estar vacía"
            )

        self._tasks.append(cleaned_description)
        logger.info(f"add(): tarea agregada exitosamente: '{cleaned_description}'")
        return True

    def delete(self, index: int) -> str:
        """
        Elimina una tarea por su índice (0-indexed).

        Args:
            index: Índice de la tarea a eliminar (0-indexed).

        Returns:
            str: Descripción de la tarea eliminada.

        Raises:
            InvalidTaskIndexError: Si el índice está fuera de rango.
            TypeError: Si index no es int.

        Example:
            >>> manager = TaskManager()
            >>> manager.add("Hacer compras")
            True
            >>> manager.delete(0)
            'Hacer compras'
        """
        if not isinstance(index, int):
            logger.error(f"delete(): tipo inválido: {type(index)}")
            raise TypeError("El índice debe ser un entero")

        if not (0 <= index < len(self._tasks)):
            logger.error(f"delete(): índice fuera de rango: {index}")
            raise InvalidTaskIndexError(
                f"El índice {index} está fuera de los límites "
                f"(0-{len(self._tasks) - 1})"
            )

        deleted_task = self._tasks.pop(index)
        logger.info(f"delete(): tarea eliminada: '{deleted_task}'")
        return deleted_task

    def is_empty(self) -> bool:
        """
        Determina si el almacén de tareas está vacío.

        Returns:
            bool: True si no hay tareas, False en caso contrario.

        Example:
            >>> manager = TaskManager()
            >>> manager.is_empty()
            True
            >>> manager.add("Una tarea")
            True
            >>> manager.is_empty()
            False
        """
        return len(self._tasks) == 0

    def count(self) -> int:
        """
        Retorna el número total de tareas.

        Returns:
            int: Cantidad de tareas en el gestor.
        """
        count = len(self._tasks)
        logger.debug(f"count(): {count} tareas totales")
        return count
