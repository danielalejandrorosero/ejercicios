

llantas = int(input("Ingrese la cantidad de llantas que desea comprar: "))
if llantas < 5:
    total = llantas * 800
else:
    total = llantas * 700
print("El total a pagar es de:", total)