"""
3) En un juego de preguntas a las que se responde “Si” o “No” gana quien responda
correctamente las tres preguntas. Si se responde mal a cualquiera de ellas ya no se pregunta
la siguiente y termina el juego. Las preguntas son:
1. Colon descubrió América?
2. La independencia de México fue en el año 1810?
3. The Doors fue un grupo de rock Americano?
"""
def jugar_preguntas():
    preguntas = [
        "¿Colon descubrió América?",
        "¿La independencia de México fue en el año 1810?",
        "¿The Doors fue un grupo de rock Americano?"
    ]
    respuestas_correctas = ["Si", "Si", "No"]
    puntaje = 0

    for i in range(len(preguntas)):
        respuesta = input(preguntas[i] + " (Si/No): ")
        if respuesta.lower() == respuestas_correctas[i].lower():
            puntaje += 1

    if puntaje == 3:
        print("¡Felicidades! Ganaste el juego.")
    else:
        print("Lo siento, perdiste el juego.")
    ver_puntaje = input("¿Deseas ver tu puntaje? (Si/No): ")

  
    if ver_puntaje.lower() == "si":
        print("Tu puntaje es:", puntaje)
    else:
        print("Gracias por jugar.")

  
jugar_preguntas()
