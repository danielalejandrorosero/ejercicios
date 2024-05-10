# Definir variables
n = int(input("Ingrese el número de vendedores: "))
sueldo_base = float(input("Ingrese el sueldo base: "))
comision = 0.10  # 10% de comisión

# Inicializar contador
i = 0

# Calcular salario de cada vendedor
while i < n:
    ventas = 3  # Número fijo de ventas por semana
    total_comisiones = ventas * sueldo_base * comision
    salario_total = sueldo_base + total_comisiones

    # Imprimir resultados
    print(f"Para el vendedor {i+1}:")
    print(f"   Comisiones por ventas: ${total_comisiones:.2f}")
    print(f"   Salario total: ${salario_total:.2f}\n")

    # Incrementar el contador
    i += 1
