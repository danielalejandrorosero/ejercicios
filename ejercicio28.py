def planificar_decisiones(capital_actual):
  if capital_actual < 0:
      saldo_deseado = 10000
  elif capital_actual < 20000:
      saldo_deseado = 20000
  else:
      saldo_deseado = capital_actual

  monto_prestamo = saldo_deseado - capital_actual

  equipo_computo = 5000
  mobiliario = 2000
  resto = (saldo_deseado - equipo_computo - mobiliario) / 2
  insumos = resto
  incentivos_personal = resto

  return insumos, incentivos_personal, monto_prestamo

capital_actual = float(input("Ingrese el capital actual de la empresa: $"))

insumos, incentivos_personal, monto_prestamo = planificar_decisiones(capital_actual)

print(f"La cantidad a destinar para la compra de insumos es: ${insumos:.2f}")
print(f"La cantidad a destinar para incentivos al personal es: ${incentivos_personal:.2f}")

if monto_prestamo > 0:
  print(f"Se pedirá un préstamo bancario por un monto de: ${monto_prestamo:.2f}")
else:
  print("No se necesita pedir ningún préstamo bancario.")





