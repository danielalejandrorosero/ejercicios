pinos_por_metro_cuadrado = 8 / 10  # 8 pinos por 10 metros cuadrados
oyameles_por_metro_cuadrado = 15 / 15  # 15 oyameles por 15 metros cuadrados
cedros_por_metro_cuadrado = 10 / 18  # 10 cedros por 18 metros cuadrados

superficie_total = float(input("Ingrese la superficie total del bosque en hectáreas: "))
superficie_metros_cuadrados = superficie_total * 10000 
if superficie_metros_cuadrados > 1000000:
    cantidad_pinos = superficie_metros_cuadrados * 0.7 * pinos_por_metro_cuadrado
    cantidad_oyameles = superficie_metros_cuadrados * 0.2 * oyameles_por_metro_cuadrado
    cantidad_cedros = superficie_metros_cuadrados * 0.1 * cedros_por_metro_cuadrado
else:
    cantidad_pinos = superficie_metros_cuadrados * 0.5 * pinos_por_metro_cuadrado
    cantidad_oyameles = superficie_metros_cuadrados * 0.3 * oyameles_por_metro_cuadrado
    cantidad_cedros = superficie_metros_cuadrados * 0.2 * cedros_por_metro_cuadrado

# Imprimir los resultados
print("Número de pinos a sembrar:", cantidad_pinos)
print("Número de oyameles a sembrar:", cantidad_oyameles)
print("Número de cedros a sembrar:", cantidad_cedros)
