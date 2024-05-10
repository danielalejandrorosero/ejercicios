def decision_compra(valor_inicial_automovil, tasa_devaluacion_automovil, tasa_incremento_terreno):
    valor_final_automovil = valor_inicial_automovil * (1 - tasa_devaluacion_automovil)**3

    valor_final_terreno = valor_inicial_automovil * (1 + tasa_incremento_terreno)**3

    if valor_final_automovil <= valor_final_terreno / 2:
        return "Deberías comprar el automóvil."
    else:
        return "No deberías comprar el automóvil."

valor_inicial = 50000  # Supongamos que el valor inicial del automóvil y el terreno es de $50,000
tasa_devaluacion = 0.1 
tasa_incremento = 0.05 

decision = decision_compra(valor_inicial, tasa_devaluacion, tasa_incremento)
print(decision)
