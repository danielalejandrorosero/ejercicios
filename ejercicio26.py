def calcular_precio_final(precio_sin_iva, marca, precio_minimo_descuento=2000):
  precio_con_descuento = precio_sin_iva

  if precio_sin_iva >= precio_minimo_descuento:
      precio_con_descuento *= 0.9

  if marca.upper() == "NOSY":
      precio_con_descuento *= 0.95

  precio_con_iva = precio_con_descuento * 1.16

  return precio_con_iva

precio_sin_iva = float(input("Ingrese el precio sin IVA del aparato: $"))
marca = input("Ingrese la marca del aparato: ")

precio_final = calcular_precio_final(precio_sin_iva, marca)
print(f"El cliente pagará ${precio_final:.2f} con IVA incluido.")
