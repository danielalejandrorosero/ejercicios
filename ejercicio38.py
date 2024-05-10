def calcular_masa_aire(presion, volumen, temperatura):
    masa = presion * volumen * 0.37 * (temperatura + 460)
    return masa

def calcular_promedio_masa_aire(vehiculos):
    total_masa_aire = 0
    contador = 0

    while contador < len(vehiculos):
        presion = float(input(f"Ingrese la presión del neumático del {vehiculos[contador]}: "))
        volumen = float(input(f"Ingrese el volumen del neumático del {vehiculos[contador]}: "))
        temperatura = float(input(f"Ingrese la temperatura del neumático del {vehiculos[contador]}: "))

        masa_aire = calcular_masa_aire(presion, volumen, temperatura)
        total_masa_aire += masa_aire

        contador += 1

    promedio_masa_aire = total_masa_aire / len(vehiculos)
    return promedio_masa_aire

# Función principal para recopilar información sobre los vehículos y calcular el promedio de masa de aire
def main():
    vehiculos = []
    continuar = 's'

    while continuar.lower() == 's':
        tipo_vehiculo = input("Ingrese el tipo de vehículo (automóvil/motocicleta): ").lower()
        vehiculos.append(tipo_vehiculo)

        continuar = input("¿Desea ingresar otro vehículo? (s/n): ")

    promedio = calcular_promedio_masa_aire(vehiculos)
    print(f"El promedio de masa de aire de los neumáticos de los {len(vehiculos)} vehículos es: {promedio:.2f}")

# Ejecutar la función principal
main()
