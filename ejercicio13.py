def pulsaciones(edad, sexo):
    if sexo == "M":
        pulsaciones = (210 - edad) / 10
    elif sexo == "F":
        pulsaciones = (220 - edad) / 10

edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (M/F): ")
pulsaciones_por_10_segundos = pulsaciones(edad, sexo)


print(pulsaciones_por_10_segundos)