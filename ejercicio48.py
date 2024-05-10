# Inicializar el contador de reprobados
reprobados = 0

# Leer las calificaciones de los 50 alumnos
contador = 1
while contador <= 50:
    calificacion = float(input(f"Ingrese la calificación del alumno {contador}: "))

    if calificacion < 70:
        reprobados += 1

    contador += 1

# Calcular el porcentaje de reprobados
porcentaje_reprobados = (reprobados / 50) * 100

# Mostrar el resultado
print(f"El porcentaje de alumnos reprobados es: {porcentaje_reprobados:.2f}%")
