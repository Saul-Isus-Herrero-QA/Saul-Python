from typing import List

class TaskManager:
    """Clase encargada de gestionar el ciclo de vida de las tareas."""
    
    def __init__(self) -> None:
        self._tasks: List[str] = []

    def get_all(self) -> List[str]:
        """Retorna la lista actual de tareas."""
        return self._tasks

    def add(self, description: str) -> bool:
        """
        Valida y añade una nueva tarea al listado.
        Retorna True si se agregó con éxito, False en caso contrario.
        """
        cleaned_description = description.strip()
        if not cleaned_description:
            return False
        self._tasks.append(cleaned_description)
        return True

    def delete(self, index: int) -> str:
        """
        Elimina una tarea por su índice de Python (0-indexed).
        Levanta un IndexError si el índice está fuera de rango.
        """
        if not (0 <= index < len(self._tasks)):
            raise IndexError("El índice de la tarea está fuera de los límites permitidos.")
        return self._tasks.pop(index)

    def is_empty(self) -> bool:
        """Determina si el almacén de tareas no contiene elementos."""
        return len(self._tasks) == 0


class CLIApplication:
    """Consola/UI Handler que interactúa con el usuario y consume el TaskManager."""
    
    def __init__(self, manager: TaskManager) -> None:
        self.manager = manager

    def show_welcome(self) -> None:
        print("====================================")
        print("       GESTOR DE TAREAS             ")
        print("====================================")
        print("Bienvenido a tu sistema de backend.\n")

    def list_tasks(self) -> None:
        print("\n--- Tu Lista de Tareas ---")
        tasks = self.manager.get_all()
        if self.manager.is_empty():
            print("[No hay tareas pendientes]")
        else:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
        print("--------------------------\n")

    def handle_add(self) -> None:
        description = input("Escribe una tarea para tu lista: ")
        if self.manager.add(description):
            print(f"¡Tarea agregada con éxito!")
        else:
            print("Error: La tarea no puede estar vacía.")

    def handle_delete(self) -> None:
        if self.manager.is_empty():
            print("No hay tareas para eliminar.")
            return

        self.list_tasks()
        try:
            display_number = int(input("Introduce el número de la tarea que deseas eliminar: "))
            target_index = display_number - 1
            
            deleted_task = self.manager.delete(target_index)
            print(f"¡Tarea '{deleted_task}' eliminada con éxito!")
            
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")
        except IndexError:
            print("Error: El número de tarea introducido no existe en el sistema.")

    def run(self) -> None:
        self.show_welcome()
        while True:
            print("¿Qué deseas hacer?")
            print("1. Agregar tarea")
            print("2. Eliminar tarea")
            print("3. Listar tareas")
            print("4. Salir")
            
            option = input("Selecciona una opción (1-4): ").strip()
            
            if option == "1":
                self.handle_add()
            elif option == "2":
                self.handle_delete()
            elif option == "3":
                self.list_tasks()
            elif option == "4":
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.\n")
                
        print("\nPrograma finalizado. ¡Buen trabajo en el backend!")


if __name__ == "__main__":
    # Inyección de dependencias limpia en el punto de entrada
    task_manager_service = TaskManager()
    app = CLIApplication(manager=task_manager_service)
    app.run()