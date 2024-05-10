import random

# Definir la población total en cada categoría de edad
poblacion_ninos = 1000
poblacion_jovenes = 2000
poblacion_adultos = 3000
poblacion_viejos = 1500

# Definir el tamaño de la muestra total
tamaño_muestra_total = 50

# Definir diccionario para almacenar las muestras de cada categoría
muestras = {
    'niños': [],
    'jóvenes': [],
    'adultos': [],
    'viejos': []
}

# Definir diccionario para almacenar las poblaciones y tamaños de muestra de cada categoría
categorias = {
    'niños': (poblacion_ninos, 0),
    'jóvenes': (poblacion_jovenes, 0),
    'adultos': (poblacion_adultos, 0),
    'viejos': (poblacion_viejos, 0)
}

# Calcular el tamaño de muestra para cada categoría de edad
for categoria, (poblacion, _) in categorias.items():
    categorias[categoria] = (poblacion, int(tamaño_muestra_total * (poblacion / (poblacion_ninos + poblacion_jovenes + poblacion_adultos + poblacion_viejos))))

# Generar muestras aleatorias para cada categoría de edad
for categoria, (poblacion, tamaño_muestra) in categorias.items():
    muestra = random.sample(range(1, poblacion+1), tamaño_muestra)
    muestras[categoria] = muestra

# Imprimir las muestras generadas
for categoria, muestra in muestras.items():
    print(f"Muestra de {categoria}: {muestra}")
