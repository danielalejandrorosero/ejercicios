"""
9) El gobierno del estado de México desea reforestar un bosque que mide determinado
numero de hectáreas. Si la superficie del terreno excede a 1 millón de metros cuadrados,
entonces decidirá sembrar de la sig. manera:
Porcentaje de la superficie del bosque Tipo de árbol
70% pino
20% oyamel
10% cedro
Si la superficie del terreno es menor o igual a un millón de metros cuadrados,
entonces decidirá sembrar de la sig. manera:
Porcentaje de la superficie del bosque Tipo de árbol
50% pino
30% oyamel
20% cedro
"""
tipo_de_arbol = ['pino', 'oyamel', 'cedro']
porcentaje = 0
def calcular_superficie_bosque(superficie_terreno):
    if superficie_terreno > 1000000:
        if porcentaje == 0.7:
            return 'pino'
        elif porcentaje == 0.2:
            return 'oyamel'
        elif porcentaje == 0.10:
            return 'cedro'
    else:
        if porcentaje == 0.50:
            return 'pino'
        elif porcentaje == 0.30:
            return 'oyamel'
        elif porcentaje == 0.20:
            return 'cedro'


superficie_terreto = int(input("Ingrese la superficie del terreno: "))
porcentaje = int(input("Ingrese el porcentaje: "))
print(calcular_superficie_bosque(superficie_terreto))

