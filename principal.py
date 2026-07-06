# Inicializamos la lista de tareas
lista_de_tareas = []
# Variable de control para el bucle
continuar = "sí"

# El bucle se ejecutará mientras la variable sea igual a "sí"
while continuar == "sí" or continuar == "si":
    nueva_tarea = input("Escribe una tarea para tu lista: ")
    lista_de_tareas.append(nueva_tarea)
    
    print("Tu lista actual es:", lista_de_tareas)
    
    # Preguntamos al usuario si desea seguir para actualizar la condición
    continuar = input("¿Quieres añadir otra tarea? (si/no): ")

print("Programa finalizado. Tus tareas guardadas son:", lista_de_tareas)