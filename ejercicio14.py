
monto = int(input("Ingrese el monto: "))
if monto < 50000:
    cuota = monto * 0.03
else:
    cuota = monto * 0.02



print(f'La cuota a pagar es: {cuota}')
