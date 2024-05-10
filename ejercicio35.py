def evaluar_apto_para_prueba():
  tiempo_por_dia = []
  for dia in range(1, 11):  # Iterar sobre los 10 días de prueba
      tiempo = float(input(f"Ingrese el tiempo en minutos del día {dia}: "))
      tiempo_por_dia.append(tiempo)

  # Verificar si en ninguna prueba hizo un tiempo mayor a 16 minutos
  if all(tiempo <= 16 for tiempo in tiempo_por_dia):
      return True

  # Verificar si al menos en una prueba hizo un tiempo mayor a 16 minutos
  if any(tiempo > 16 for tiempo in tiempo_por_dia):
      return True

  # Calcular el promedio de tiempos
  promedio_tiempo = sum(tiempo_por_dia) / len(tiempo_por_dia)

  # Verificar si el promedio de tiempos es menor o igual a 15 minutos
  if promedio_tiempo <= 15:
      return True

  # Si no cumple ninguna condición, retornar False
  return False

# Ejemplo de uso
if evaluar_apto_para_prueba():
  print("El atleta es apto para la prueba de 5 kilómetros.")
else:
  print("El atleta debe buscar otra especialidad.")
