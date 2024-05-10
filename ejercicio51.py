# Inicializar contadores de votos para cada candidato
votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0

# Leer los 250,000 votos
total_votos = 250000
voto_actual = 1
while voto_actual <= total_votos:
    voto = int(input(f"Ingrese el número del candidato por el cual votó el votante {voto_actual} (1/2/3): "))

    # Incrementar el contador de votos del candidato correspondiente
    if voto == 1:
        votos_candidato_1 += 1
    elif voto == 2:
        votos_candidato_2 += 1
    elif voto == 3:
        votos_candidato_3 += 1

    voto_actual += 1

# Determinar al candidato ganador


ganador = 1
cantidad_votos_ganador = votos_candidato_1

if votos_candidato_2 > cantidad_votos_ganador:
    ganador = 2
    cantidad_votos_ganador = votos_candidato_2

if votos_candidato_3 > cantidad_votos_ganador:
    ganador = 3
    cantidad_votos_ganador = votos_candidato_3

# Imprimir el número del candidato ganador y su cantidad de votos
print(f"El candidato ganador es el candidato {ganador} con {cantidad_votos_ganador} votos.")
