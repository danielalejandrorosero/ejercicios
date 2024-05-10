"""
4) Calcular el numero de pulsaciones que una persona debe tener por cada 10 segundos de
ejercicio, si la formula es:
num. pulsaciones = (220 - edad)/10
"""


num_pulsaciones = 0
edad = int(input('Ingrese su edad: '))

num_pulsaciones = (220 - edad) / 10

print(num_pulsaciones)