def encontrar_numero_medio(num1, num2, num3):
  if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
      return num1
  elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
      return num2
  else:
      return num3

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

numero_medio = encontrar_numero_medio(num1, num2, num3)

print(f"El número medio es: {numero_medio}")
