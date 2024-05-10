

def calcular_porcentaje_animales():
  especies = ["elefantes", "jirafas", "chimpancés"]
  muestras_por_especie = {"elefantes": 20, "jirafas": 15, "chimpancés": 40}

  for especie in especies:
      categoria_0_1 = int(input(f"Ingrese la cantidad de animales de 0 a 1 año de {especie}: "))
      categoria_1_3 = int(input(f"Ingrese la cantidad de animales de más de 1 año y menos de 3 de {especie}: "))
      categoria_3_mas = int(input(f"Ingrese la cantidad de animales de 3 o más años de {especie}: "))

      total_muestras = muestras_por_especie[especie]
      porcentaje_0_1 = (categoria_0_1 / total_muestras) * 100
      porcentaje_1_3 = (categoria_1_3 / total_muestras) * 100
      porcentaje_3_mas = (categoria_3_mas / total_muestras) * 100

      print(f"Porcentaje de animales de 0 a 1 año de {especie}: {porcentaje_0_1:.2f}%")
      print(f"Porcentaje de animales de más de 1 año y menos de 3 de {especie}: {porcentaje_1_3:.2f}%")
      print(f"Porcentaje de animales de 3 o más años de {especie}: {porcentaje_3_mas:.2f}%")
      print()

# Ejemplo de uso
calcular_porcentaje_animales()
