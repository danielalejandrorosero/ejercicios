"""
2) En una llantera se ha establecido una promoción de las llantas marca “Ponchadas”, dicha
promoción consiste en lo siguiente:
Si se compran menos de cinco llantas el precio es de $300 cada una, de $250 si se
compran de cinco a 10 y de $200 si se compran mas de 10.
Obtener la cantidad de dinero que una persona tiene que pagar por cada una de las
llantas que compra y la que tiene que pagar por el total de la compra.
"""
def calcular_total_pagar(num_llantas):
    if num_llantas < 5:
        precio_unitario = 300
    elif num_llantas <= 10:
        precio_unitario = 250
    else:
        precio_unitario = 200

    total_pagar = num_llantas * precio_unitario

    return total_pagar


# Ejemplo de uso  
cantidad_llantas = int(input("Ingrese la cantidad de llantas a comprar: "))
total_pagar = calcular_total_pagar(cantidad_llantas)
print(f'El total a pagar por {cantidad_llantas} llantas es: ${total_pagar}')