def calcular_salario_semanal(horas_trabajadas, salario_por_hora):
    if horas_trabajadas <= 40:
        salario_semanal = horas_trabajadas * salario_por_hora
    else:
        horas_normales = 40
        horas_extra = horas_trabajadas - 40
        salario_semanal = (horas_normales * salario_por_hora) + (horas_extra * salario_por_hora * 2)
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
