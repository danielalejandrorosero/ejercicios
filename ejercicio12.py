
import random

numero_azar = random.randint(1, 100)
descuento =  0
if numero_azar < 74:
    descuento = 0.15
elif numero_azar >74:
  descuento = 0.20



print(f'El numero escogido es {numero_azar} y el descuento es {descuento}')