
clientes = 15

descuento = 0.15

precio_por_kilo = 10 

total_percibido = 0

for cliente in range(clientes):
    kilos_comprados = float(input(f"Ingrese la cantidad de kilos comprados por el cliente {cliente + 1}: "))

    precio_sin_descuento = kilos_comprados * precio_por_kilo

    if kilos_comprados > 10:
        precio_con_descuento = precio_sin_descuento * (1 - descuento)
    else:
        precio_con_descuento = precio_sin_descuento

    print(f"El cliente {cliente + 1} pagará: ${precio_con_descuento}")

    total_percibido += precio_con_descuento

print(f"El total percibido por la tienda es: ${total_percibido}")
