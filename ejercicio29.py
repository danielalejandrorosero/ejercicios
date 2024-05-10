def determinar_anemia(edad, sexo, nivel_hemoglobina):
  if edad <= 0: 
      return "Edad no válida"

  if sexo.lower() not in ['m', 'f']: 
      return "Sexo no válido"

  if edad <= 1:
      if nivel_hemoglobina < 13 or nivel_hemoglobina > 26:
          return "Positivo"
      else:
          return "Negativo"
  elif edad <= 6: 
      if nivel_hemoglobina < 10 or nivel_hemoglobina > 18:
          return "Positivo"
      else:
          return "Negativo"
  elif edad <= 12:
      if nivel_hemoglobina < 11 or nivel_hemoglobina > 15:
          return "Positivo"
      else:
          return "Negativo"
  elif edad <= 5: 
      if nivel_hemoglobina < 11.5 or nivel_hemoglobina > 15:
          return "Positivo"
      else:
          return "Negativo"
  elif edad <= 10: 
      if nivel_hemoglobina < 12.6 or nivel_hemoglobina > 15.5:
          return "Positivo"
      else:
          return "Negativo"
  elif edad <= 15: 
      if nivel_hemoglobina < 13 or nivel_hemoglobina > 15.5:
          return "Positivo"
      else:
          return "Negativo"
  else: 
      if sexo.lower() == 'f':  
          if nivel_hemoglobina < 12 or nivel_hemoglobina > 16:
              return "Positivo"
          else:
              return "Negativo"
      else: 
          if nivel_hemoglobina < 14 or nivel_hemoglobina > 18:
              return "Positivo"
          else:
              return "Negativo"

resultado = determinar_anemia(25, 'M', 19.5)
print("Resultado de análisis de anemia:", resultado)
