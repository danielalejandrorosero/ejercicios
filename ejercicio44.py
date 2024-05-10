def obtener_porcentaje_estudios(total_personas, nivel_educativo):
    porcentaje = (nivel_educativo / total_personas) * 100
    return porcentaje

# Función principal para recopilar datos y calcular porcentajes
def main():
    total_personas = int(input("Ingrese el número total de personas encuestadas: "))

    primaria = 0
    secundaria = 0
    carrera_tecnica = 0
    estudios_profesionales = 0
    posgrado = 0

    contador = 0
    while contador < total_personas:
        nivel_educativo = input(f"Ingrese el nivel educativo de la persona {contador + 1} (primaria/secundaria/carrera técnica/estudios profesionales/posgrado): ").lower()

        if nivel_educativo == "primaria":
            primaria += 1
        elif nivel_educativo == "secundaria":
            secundaria += 1
        elif nivel_educativo == "carrera técnica" or nivel_educativo == "carrera tecnica":
            carrera_tecnica += 1
        elif nivel_educativo == "estudios profesionales":
            estudios_profesionales += 1
        elif nivel_educativo == "posgrado":
            posgrado += 1

        contador += 1

    porcentaje_primaria = obtener_porcentaje_estudios(total_personas, primaria)
    porcentaje_secundaria = obtener_porcentaje_estudios(total_personas, secundaria)
    porcentaje_carrera_tecnica = obtener_porcentaje_estudios(total_personas, carrera_tecnica)
    porcentaje_estudios_profesionales = obtener_porcentaje_estudios(total_personas, estudios_profesionales)
    porcentaje_posgrado = obtener_porcentaje_estudios(total_personas, posgrado)

    print(f"Porcentaje de personas con estudios de primaria: {porcentaje_primaria:.2f}%")
    print(f"Porcentaje de personas con estudios de secundaria: {porcentaje_secundaria:.2f}%")
    print(f"Porcentaje de personas con estudios de carrera técnica: {porcentaje_carrera_tecnica:.2f}%")
    print(f"Porcentaje de personas con estudios profesionales: {porcentaje_estudios_profesionales:.2f}%")
    print(f"Porcentaje de personas con estudios de posgrado: {porcentaje_posgrado:.2f}%")

# Ejecutar la función principal
main()
