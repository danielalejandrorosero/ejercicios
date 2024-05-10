def calcular_total_a_pagar():
  total_a_pagar = 0

  continuar_comprando = True
  while continuar_comprando:
      precio = float(input("Ingrese el precio del artículo: "))
      etiqueta = input("Ingrese el color de la etiqueta (roja/otro): ").lower()

      if etiqueta == "roja":
          precio_con_descuento = precio * 0.8  # Aplicar descuento del 20%
          print(f"Este artículo tiene un 20% de descuento. Precio con descuento: ${precio_con_descuento:.2f}")
          total_a_pagar += precio_con_descuento
      else:
          total_a_pagar += precio

      continuar = input("¿Desea seguir comprando? (s/n): ").lower()
      if continuar != "s":
          continuar_comprando = False

  return total_a_pagar

# Función principal para controlar las compras en la tienda
def main():
  total_a_pagar = calcular_total_a_pagar()
  print(f"La cantidad total a pagar es: ${total_a_pagar:.2f}")

# Ejecutar la función principal
main()
