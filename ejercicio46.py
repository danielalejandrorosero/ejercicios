def verificar_limite_de_produccion(tipo_impresion, copias_pendientes, copias_solicitadas):
    limite_de_produccion = 10000 if tipo_impresion == "offset" else 50000
    total_copias = copias_pendientes + copias_solicitadas

    if total_copias <= limite_de_produccion:
        print("El trabajo solicitado puede ser aceptado.")
        return True
    else:
        print("El límite de producción se excedería. El trabajo solicitado no puede ser aceptado.")
        return False

# Función principal para llevar el control de las copias solicitadas
def main():
    continuar = True

    while continuar:
        copias_pendientes = int(input("Ingrese el número de copias pendientes hasta el momento: "))
        tipo_impresion = input("Ingrese el tipo de impresión (offset/estándar): ").lower()
        copias_solicitadas = int(input("Ingrese el número de copias solicitadas en el día: "))

        verificar_limite_de_produccion(tipo_impresion, copias_pendientes, copias_solicitadas)

        respuesta = input("¿Desea ingresar otra solicitud de trabajo? (s/n): ").lower()
        if respuesta != "s":
            continuar = False

# Ejecutar la función principal
main()
