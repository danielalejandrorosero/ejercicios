
"""
3) La presión, el volumen y la temperatura de una masa de aire se relacionan por la
formula:
masa = (presión * volumen)/(0.37 * (temperatura + 460))
"""

def calcular_masa(presion, volumen, temperatura):
  masa = (presion * volumen) / (0.37 * (temperatura + 460))
  return masa


presion = float(input('Ingrese la presión: '))
volumen = float(input('Ingrese el volumen: '))
temperatura = float(input('Ingrese la temperatura: '))

masa_calculada = calcular_masa(presion, volumen, temperatura)
print(f' la masa de aire es:', masa_calculada)
