def calcular_calidad(peso_gallina, altura_gallina, huevos_por_semana):
    calidad = (peso_gallina * altura_gallina) / huevos_por_semana
    return calidad

def calcular_precio_kilo_huevo(promedio_calidad):
    if promedio_calidad >= 15:
        precio_por_kilo = 1.2 * promedio_calidad
    elif promedio_calidad > 8 and promedio_calidad < 15:
        precio_por_kilo = 1.0 * promedio_calidad
    else:
        precio_por_kilo = 0.8 * promedio_calidad
    return precio_por_kilo

def calcular_promedio_calidad_gallinas(n):
    total_calidad = 0
    contador = 0
    while contador < n:
        peso_gallina = float(input(f"Ingrese el peso de la gallina {contador + 1}: "))
        altura_gallina = float(input(f"Ingrese la altura de la gallina {contador + 1}: "))
        huevos_por_semana = int(input(f"Ingrese el número de huevos que pone la gallina {contador + 1} por semana: "))

        calidad = calcular_calidad(peso_gallina, altura_gallina, huevos_por_semana)
        total_calidad += calidad

        contador += 1

    promedio_calidad = total_calidad / n
    return promedio_calidad

# Función principal para determinar el precio de venta por kilo de huevo
def main():
    n = int(input("Ingrese el número de gallinas en la granja: "))
    promedio_calidad = calcular_promedio_calidad_gallinas(n)
    precio_kilo_huevo = calcular_precio_kilo_huevo(promedio_calidad)

    print(f"El precio de venta por kilo de huevo es: ${precio_kilo_huevo:.2f}")

# Ejecutar la función principal
main()
