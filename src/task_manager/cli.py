"""Interfaz de línea de comandos para la aplicación de gestor de tareas."""

import logging
from typing import Optional

from .exceptions import EmptyTaskDescriptionError, InvalidTaskIndexError
from .models import TaskManager

logger = logging.getLogger(__name__)


class CLIApplication:
    """
    Manejador de consola/UI que interactúa con el usuario.

    Consume el TaskManager y proporciona una interfaz amigable
    para gestionar tareas desde la línea de comandos.

    Attributes:
        manager: Instancia de TaskManager inyectada.
    """

    def __init__(self, manager: TaskManager) -> None:
        """
        Inicializa la aplicación CLI.

        Args:
            manager: Instancia del gestor de tareas a usar.
        """
        self.manager = manager
        logger.info("CLIApplication inicializada")

    def show_welcome(self) -> None:
        """Muestra el mensaje de bienvenida."""
        print("\n" + "=" * 40)
        print("    GESTOR DE TAREAS")
        print("=" * 40)
        print("Bienvenido a tu sistema de backend.\n")
        logger.info("Mensaje de bienvenida mostrado")

    def list_tasks(self) -> None:
        """Muestra todas las tareas del sistema."""
        print("\n--- Tu Lista de Tareas ---")
        tasks = self.manager.get_all()

        if self.manager.is_empty():
            print("[No hay tareas pendientes]")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

        print(f"Total: {self.manager.count()} tarea(s)")
        print("-" * 25 + "\n")
        logger.debug(f"Listado mostrado con {self.manager.count()} tareas")

    def handle_add(self) -> None:
        """Maneja la adición de una nueva tarea."""
        try:
            description = input(" Escribe una tarea para tu lista: ").strip()

            if not description:
                print("Error: La tarea no puede estar vacía.")
                logger.warning("Intento de agregar tarea vacía")
                return

            self.manager.add(description)
            print("¡Tarea agregada con éxito!")

        except EmptyTaskDescriptionError as e:
            print(f"Error: {e}")
            logger.error(f"Error al agregar tarea: {e}")
        except TypeError as e:
            print(f"Error de tipo: {e}")
            logger.error(f"Error de tipo: {e}")

    def handle_delete(self) -> None:
        """Maneja la eliminación de una tarea."""
        if self.manager.is_empty():
            print("No hay tareas para eliminar.")
            logger.info("Intento de eliminar en lista vacía")
            return

        try:
            self.list_tasks()
            user_input = input("Introduce el número de la tarea a eliminar: ").strip()

            if not user_input:
                print("Error: Debes ingresar un número.")
                return

            task_number = int(user_input)
            target_index = task_number - 1

            deleted_task = self.manager.delete(target_index)
            print(f"¡Tarea '{deleted_task}' eliminada con éxito!")

        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")
            logger.warning(f"Intento de eliminación con valor inválido: {user_input}")
        except InvalidTaskIndexError as e:
            print(f"Error: {e}")
            logger.warning(f"Intento de eliminación con índice inválido: {e}")

    def show_menu(self) -> None:
        """Muestra el menú principal."""
        print("¿Qué deseas hacer?")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Listar tareas")
        print("4️. Salir")

    def _get_valid_option(self) -> str:
        """
        Obtiene una opción válida del usuario.

        Returns:
            str: Opción elegida (1-4).
        """
        while True:
            option = input("Selecciona una opción (1-4): ").strip()
            if option in ("1", "2", "3", "4"):
                return option
            print("Opción no válida. Inténtalo de nuevo.\n")
            logger.warning(f"Opción inválida ingresada: {option}")

    def run(self) -> None:
        """Ejecuta el bucle principal de la aplicación."""
        self.show_welcome()
        logger.info("Aplicación iniciada - ingresando bucle principal")

        try:
            while True:
                self.show_menu()
                option = self._get_valid_option()

                if option == "1":
                    self.handle_add()
                elif option == "2":
                    self.handle_delete()
                elif option == "3":
                    self.list_tasks()
                elif option == "4":
                    print("\n ¡Hasta luego! ¡Buen trabajo en el backend!\n")
                    logger.info("Aplicación cerrada por el usuario")
                    break

        except KeyboardInterrupt:
            print("\n\n Aplicación interrumpida por el usuario (Ctrl+C)")
            logger.info("Aplicación interrumpida por KeyboardInterrupt")
        except Exception as e:
            print(f"\n Error inesperado: {e}")
            logger.exception(f"Error inesperado en el bucle principal: {e}")
