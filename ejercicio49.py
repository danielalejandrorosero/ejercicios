# Inicializar variables para el alumno con el mayor promedio
numero_control_mayor_promedio = ""
mayor_promedio = float('-inf')

unidad = 1
while unidad <= 5:
    print(f"Unidad {unidad}:")
    alumno = 1
    while alumno <= 5:
        numero_control = input(f"Ingrese el número de control del alumno {alumno} en la unidad {unidad}: ")
        calificacion = float(input(f"Ingrese la calificación del alumno {alumno} en la unidad {unidad}: "))

        # Calcular el promedio del alumno
        promedio = calificacion / 5

        # Actualizar al alumno con el mayor promedio
        if promedio > mayor_promedio:
            numero_control_mayor_promedio = numero_control
            mayor_promedio = promedio

        alumno += 1

    unidad += 1

# Mostrar el número de control del alumno con el mayor promedio
print(f"El número de control del alumno con el mayor promedio es: {numero_control_mayor_promedio}")
