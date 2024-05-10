def calcular_descuento(num_computadoras):
  if num_computadoras < 5:
      descuento = 0.10
  elif num_computadoras >=5 and num_computadoras < 10:
      descuento = 0.20
  else:
      descuento = 0.40
  return descuento

precio_computadora = 11000

computadoras_compradas = int(input("Ingrese el número de computadoras compradas: "))

descuento = calcular_descuento(computadoras_compradas)

total_compra = computadoras_compradas * precio_computadora

monto_descuento = total_compra * descuento
total_a_pagar = total_compra - monto_descuento

print("Total de la compra:", total_compra)
print("Descuento aplicado:", descuento * 100, "%")
print("Monto del descuento:", monto_descuento)
print("Total a pagar después del descuento:", total_a_pagar)
