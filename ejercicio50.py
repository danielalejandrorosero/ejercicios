# Inicializar contador de alumnos sin derecho al examen de nivelación
sin_derecho = 0

# Iterar sobre los 40 alumnos
alumno = 1
while alumno <= 40:
    print(f"Alumno {alumno}:")

    # Inicializar bandera para verificar si el alumno tiene derecho al examen de nivelación
    derecho = True

    # Leer las calificaciones de las 5 unidades
    unidad = 1
    while unidad <= 5:
        calificacion = float(input(f"Ingrese la calificación de la unidad {unidad}: "))

        # Verificar si la calificación es menor que 70
        if calificacion < 70:
            derecho = False

        unidad += 1

    # Verificar si el alumno tiene derecho al examen de nivelación
    if not derecho:
        sin_derecho += 1

    alumno += 1

# Mostrar la cantidad de alumnos que no tienen derecho al examen de nivelación
print(f"La cantidad de alumnos que no tienen derecho al examen de nivelación es: {sin_derecho}")
