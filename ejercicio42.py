def calcular_porcentajes_encuesta(n, opiniones):
    a_favor = 0
    en_contra = 0
    abstencion = 0

    contador = 0
    while contador < n:
        opinion = input(f"Ingrese la opinión del diputado {contador + 1} (a favor/en contra/abstención): ").lower()

        if opinion == "a favor":
            a_favor += 1
        elif opinion == "en contra":
            en_contra += 1
        elif opinion == "abstencion" or opinion == "abstención":
            abstencion += 1

        contador += 1

    porcentaje_a_favor = (a_favor / n) * 100
    porcentaje_en_contra = (en_contra / n) * 100
    porcentaje_abstencion = (abstencion / n) * 100

    return porcentaje_a_favor, porcentaje_en_contra, porcentaje_abstencion

# Función principal para levantar la encuesta en la Cámara de Diputados
def main():
    n = int(input("Ingrese el número total de diputados: "))
    opiniones = []
    porcentaje_a_favor, porcentaje_en_contra, porcentaje_abstencion = calcular_porcentajes_encuesta(n, opiniones)

    print(f"Porcentaje de diputados a favor: {porcentaje_a_favor:.2f}%")
    print(f"Porcentaje de diputados en contra: {porcentaje_en_contra:.2f}%")
    print(f"Porcentaje de diputados que se abstienen de opinar: {porcentaje_abstencion:.2f}%")

# Ejecutar la función principal
main()
