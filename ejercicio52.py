# Inicializar variables para el total de ventas y el número de clientes atendidos
total_ventas = 0
clientes_atendidos = 0

# Leer las ventas de los clientes hasta que se termine el día
while True:
    monto_compra = float(input("Ingrese el monto total de la compra del cliente (o ingrese 0 para finalizar): "))

    # Si el monto de la compra es 0, se termina el día
    if monto_compra == 0:
        break

    # Registrar la venta y al cliente atendido
    total_ventas += monto_compra
    clientes_atendidos += 1

# Mostrar el total de ventas y el número de clientes atendidos al final del día
print(f"La cantidad total de ventas del día es: {total_ventas}")
print(f"El número de clientes atendidos es: {clientes_atendidos}")
