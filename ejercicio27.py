def calcular_descuento(num_kilos):
  if num_kilos <= 2:
      descuento = 0.00
  elif num_kilos <= 5:
      descuento = 0.10
  elif num_kilos <= 10:
      descuento = 0.15
  else:
      descuento = 0.20
  return descuento

precio_por_kilo = 100 

kilos_comprados = float(input("Ingrese la cantidad de kilos de manzanas comprados: "))

descuento = calcular_descuento(kilos_comprados)

precio_total = kilos_comprados * precio_por_kilo * (1 - descuento)

print("El precio total a pagar es:", precio_total, "pesos.")
