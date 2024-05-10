def calcular_promedio_puntos_contaminantes(cantidad_carros):
  total_puntos_contaminantes = 0
  carros_contaminados = 0
  puntos_contaminantes_por_carro = []

  for i in range(cantidad_carros):
      puntos_contaminantes = float(input(f"Ingrese los puntos contaminantes del carro {i + 1}: "))
      puntos_contaminantes_por_carro.append(puntos_contaminantes)

      total_puntos_contaminantes += puntos_contaminantes
      if puntos_contaminantes >= 25:
          carros_contaminados += 1

  promedio_puntos_contaminantes = total_puntos_contaminantes / cantidad_carros
  min_contaminantes = min(puntos_contaminantes_por_carro)
  max_contaminantes = max(puntos_contaminantes_por_carro)

  return promedio_puntos_contaminantes, carros_contaminados, min_contaminantes, max_contaminantes

promedio, carros_contaminados, min_contaminantes, max_contaminantes = calcular_promedio_puntos_contaminantes(cantidad_carros=25)
print(f"Promedio de puntos contaminantes: {promedio}")
print(f"Carros con más de 25 puntos contaminantes: {carros_contaminados}")
print(f"Puntos contaminantes del carro que menos contaminó: {min_contaminantes}")
print(f"Puntos contaminantes del carro que más contaminó: {max_contaminantes}")
