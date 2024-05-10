# Función principal para recopilar datos y determinar la sección con más votantes
def main():
    secciones = ["norte", "sur", "centro"]
    votantes_por_seccion = {seccion: 0 for seccion in secciones}

    continuar_ingreso = True
    while continuar_ingreso:
        seccion = input("Ingrese la sección a la que pertenece el votante (norte/sur/centro): ").lower()
        if seccion in secciones:
            votantes_por_seccion[seccion] += 1
        else:
            print("Sección inválida. Por favor, ingrese una sección válida.")

        continuar = input("¿Desea ingresar otro votante? (s/n): ").lower()
        if continuar != "s":
            continuar_ingreso = False

    # Calcular la sección con mayor número de votantes
    seccion_max_votantes = max(votantes_por_seccion, key=votantes_por_seccion.get)

    # Mostrar resultados
    print("Número de votantes por sección:")
    for seccion, votantes in votantes_por_seccion.items():
        print(f"{seccion.capitalize()}: {votantes}")

    print(f"La sección con mayor número de votantes es: {seccion_max_votantes.capitalize()}")

# Ejecutar la función principal
main()
