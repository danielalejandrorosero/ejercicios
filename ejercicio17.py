def calcular_deposito_sar(salario_mensual, porcentaje_empleador, porcentaje_trabajador):
  total_deposito = salario_mensual * (porcentaje_empleador + porcentaje_trabajador)

  pago_mensual = salario_mensual - total_deposito

  return total_deposito, pago_mensual

salario_mensual = int(input("Ingrese el salario mensual del trabajador: "))
porcentaje_empleador = int(input("Ingrese el porcentaje que el empleador debe depositar en el SAR (en decimal): "))
porcentaje_trabajador = int(input("Ingrese el porcentaje que el trabajador aportará al SAR (en decimal): "))

total_deposito, pago_mensual = calcular_deposito_sar(salario_mensual, porcentaje_empleador, porcentaje_trabajador)

print("Cantidad total depositada en la cuenta del SAR cada mes:", total_deposito)
print("Pago mensual que recibirá el trabajador:", pago_mensual)
