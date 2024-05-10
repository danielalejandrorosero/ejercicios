"""
Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas
invierte una cantidad distinta. Obtener el porcentaje que cada quien invierte con
respecto a la cantidad total invertida.
"""

def calcular_porcentaje(inversion1, inversion2, inversion3):
  total_invertido = inversion1 + inversion2 + inversion3
  print(f'el total invertido es: {total_invertido} ')
  porcentaje1 = inversion1 / total_invertido * 100
  porcentaje2 = inversion2 / total_invertido * 100
  porcentaje3 = inversion3 / total_invertido * 100
  return porcentaje1, porcentaje2, porcentaje3



inversion1 = int(input("Ingrese la cantidad invertida por la primera persona: "))
inversion2 = int(input("Ingrese la cantidad invertida por la segunda persona: "))
inversion3 = int(input("Ingrese la cantidad invertida por la tercera persona: "))

porcentaje1, porcentaje2, porcentaje3 = calcular_porcentaje(inversion1, inversion2, inversion3)

print(f'El porcentaje invertido por la primera persona es: {porcentaje1}%')
print(f'El porcentaje invertido por la segunda persona es: {porcentaje2}%')
print(f'El porcentaje invertido por la tercera persona es: {porcentaje3}%')


