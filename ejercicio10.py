matematicas_examen = float(input("Ingrese la calificación del examen de Matemáticas: "))
matematicas_tareas = sum([float(input(f"Ingrese la calificación de la tarea {i+1} de Matemáticas: ")) for i in range(3)]) / 3

fisica_examen = float(input("Ingrese la calificación del examen de Física: "))
fisica_tareas = sum([float(input(f"Ingrese la calificación de la tarea {i+1} de Física: ")) for i in range(2)]) / 2

quimica_examen = float(input("Ingrese la calificación del examen de Química: "))
quimica_tareas = sum([float(input(f"Ingrese la calificación de la tarea {i+1} de Química: ")) for i in range(3)]) / 3

promedio_matematicas = matematicas_examen * 0.9 + matematicas_tareas * 0.1
promedio_fisica = fisica_examen * 0.8 + fisica_tareas * 0.2
promedio_quimica = quimica_examen * 0.85 + quimica_tareas * 0.15

promedio_general = (promedio_matematicas + promedio_fisica + promedio_quimica) / 3

print("El promedio en Matemáticas es:", promedio_matematicas)
print("El promedio en Física es:", promedio_fisica)
print("El promedio en Química es:", promedio_quimica)
print("El promedio general es:", promedio_general)  
