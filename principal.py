def mostrar_bienvenida():
    """Imprime el saludo inicial de la aplicación."""
    print("====================================")
    print("       GESTOR DE TAREAS v1.0        ")
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


def ejecutar_gestor():
    """Función principal que controla el flujo de la aplicación."""
    lista_de_tareas = []
    continuar = "sí"
    
    mostrar_bienvenida()
    
    while continuar.lower() in ["sí", "si", "s", "yes", "y"]:
        agregar_tarea(lista_de_tareas)
        listar_tareas(lista_de_tareas)
        
        continuar = input("¿Quieres añadir otra tarea? (sí/no): ")
        
    print("\nPrograma finalizado. ¡Buen trabajo con tus tareas!")


# Punto de entrada estándar en Python profesional
if __name__ == "__main__":
    ejecutar_gestor()