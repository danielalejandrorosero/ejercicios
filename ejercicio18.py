def calcular_inversion(monto_hipoteca):
    if monto_hipoteca < 1000000:
        inversion_persona = monto_hipoteca / 2
        inversion_socio = monto_hipoteca / 2
    else:
        inversion_persona = monto_hipoteca
        inversion_socio = (monto_hipoteca - 1000000) / 2

    return inversion_persona, inversion_socio

monto_hipoteca = int(input("Ingrese el monto de la hipoteca: "))

inversion_persona, inversion_socio = calcular_inversion(monto_hipoteca)

print("La persona invertirá: $", inversion_persona)
print("El socio invertirá: $", inversion_socio)
