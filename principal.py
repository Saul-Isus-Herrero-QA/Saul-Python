def mostrar_bienvenida():
    """Imprime el saludo inicial de la aplicación."""
    print("====================================")
    print("       GESTOR DE TAREAS v1.1        ")
    print("====================================")
    print("Bienvenido a tu sistema de backend.\n")


def listar_tareas(lista):
    """Muestra las tareas actuales de la lista de forma numerada."""
    print("\n--- Tu Lista de Tareas ---")
    if not lista:
        print("[No hay tareas pendientes]")
    else:
        for indice, tarea in enumerate(lista):
            print(f"{indice + 1}. {tarea}")
    print("--------------------------\n")


def agregar_tarea(lista):
    """Solicita una nueva tarea al usuario y la añade a la lista."""
    nueva_tarea = input("Escribe una tarea para tu lista: ")
    if nueva_tarea.strip():  # Valida que no esté vacía
        lista.append(nueva_tarea)
        print(f"¡Tarea '{nueva_tarea}' agregada con éxito!")
    else:
        print("Error: La tarea no puede estar vacía.")


def eliminar_tarea(lista):
    """Solicita el número de una tarea y la elimina de la lista si existe."""
    if not lista:
        print("No hay tareas para eliminar.")
        return

    listar_tareas(lista)
    try:
        # El usuario ve las tareas enumeradas desde 1, pero Python indexa desde 0
        numero_tarea = int(input("Introduce el número de la tarea que deseas eliminar: "))
        indice = numero_tarea - 1
        
        if 0 <= indice < len(lista):
            tarea_eliminada = lista.pop(indice)
            print(f"¡Tarea '{tarea_eliminada}' eliminada con éxito!")
        else:
            print("Error: El número de tarea introducido no existe.")
    except ValueError:
        print("Error: Por favor, introduce un número válido.")


def ejecutar_gestor():
    """Función principal que controla el flujo de la aplicación."""
    lista_de_tareas = []
    
    mostrar_bienvenida()
    
    while True:
        print("¿Qué deseas hacer?")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Listar tareas")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == "1":
            agregar_tarea(lista_de_tareas)
        elif opcion == "2":
            eliminar_tarea(lista_de_tareas)
        elif opcion == "3":
            listar_tareas(lista_de_tareas)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.\n")
        
    print("\nPrograma finalizado. ¡Buen trabajo con tus tareas!")


# Punto de entrada estándar en Python profesional
if __name__ == "__main__":
    ejecutar_gestor()