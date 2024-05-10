def calcular_pago_casa(ingresos, costo_casa):
  if ingresos < 8000:
      enganche = 0.15 * costo_casa
      monto_a_financiar = costo_casa - enganche
      numero_de_pagos = 120  # 10 años * 12 meses
  else:
      enganche = 0.30 * costo_casa
      monto_a_financiar = costo_casa - enganche
      numero_de_pagos = 84  # 7 años * 12 meses

  pago_mensual = monto_a_financiar / numero_de_pagos

  return enganche, pago_mensual

ingresos_comprador = int(input("Ingrese los ingresos del comprador: "))
costo_casa = int(input("Ingrese el costo de la casa: "))

enganche, pago_mensual = calcular_pago_casa(ingresos_comprador, costo_casa)

print("El comprador debe pagar un enganche de:", enganche)
print("El comprador debe pagar mensualmente:", pago_mensual)

