def calcular_salario_semanal(horas_trabajadas, salario_por_hora):
    horas_normales = min(horas_trabajadas, 40)  # Máximo de 40 horas normales
    horas_extra = max(horas_trabajadas - 40, 0)  # Horas extras (máximo de 8)
    horas_extra_triple = max(horas_extra - 8, 0)  # Horas extras pagadas al triple

    # Calcular salario por horas normales y horas extras
    salario_horas_normales = horas_normales * salario_por_hora
    salario_horas_extra_doble = min(horas_extra, 8) * salario_por_hora * 2
    salario_horas_extra_triple = horas_extra_triple * salario_por_hora * 3

    # Calcular salario total
    salario_semanal = salario_horas_normales + salario_horas_extra_doble + salario_horas_extra_triple
    return salario_semanal

def calcular_salarios_obreros(n):
    salarios = []
    contador = 1
    while contador <= n:
        horas_trabajadas = float(input(f"Ingrese las horas trabajadas por el obrero {contador} esta semana: "))
        salario_por_hora = float(input(f"Ingrese el salario por hora del obrero {contador}: "))
        salario_semanal = calcular_salario_semanal(horas_trabajadas, salario_por_hora)
        salarios.append(salario_semanal)
        contador += 1
    return salarios

# Función principal para calcular los salarios semanales de los obreros
def main():
    n = int(input("Ingrese el número de obreros: "))
    salarios = calcular_salarios_obreros(n)

    contador = 1
    while contador <= n:
        print(f"El obrero {contador} recibirá ${salarios[contador - 1]:.2f} esta semana.")
        contador += 1

# Ejecutar la función principal
main()
