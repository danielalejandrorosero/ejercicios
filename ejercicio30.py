def calcular_colegiatura(promedio, tipo_alumno):
  unidades = 0
  descuento = 0

  if tipo_alumno == "preparatoria":
      if promedio >= 9.5:
          unidades = 55
          descuento = 0.25
      elif promedio >= 9:
          unidades = 50
          descuento = 0.10
      elif promedio > 7:
          unidades = 50
      elif promedio <= 7 and promedio >= 0 and reprobadas >= 0 and reprobadas <= 3:
          unidades = 45
      elif promedio <= 7 and promedio >= 0 and reprobadas >= 4:
          unidades = 40
  elif tipo_alumno == "profesional":
      if promedio >= 9.5:
          unidades = 55
          descuento = 0.20
      else:
          unidades = 55

  if unidades == 0:
      return "No es posible determinar el total debido a datos incorrectos."

  colegiatura_por_unidad = 180 if tipo_alumno == "preparatoria" else 300
  costo_total = (unidades / 5) * colegiatura_por_unidad

  if descuento > 0:
      costo_total -= costo_total * descuento

  return costo_total

tipo_alumno = input("Ingrese el tipo de alumno (preparatoria o profesional): ").lower()
promedio = float(input("Ingrese el promedio del alumno: "))

if tipo_alumno == "preparatoria":
  reprobadas = int(input("Ingrese el número de materias reprobadas: "))

total_a_pagar = calcular_colegiatura(promedio, tipo_alumno)
print(f"El total a pagar por la colegiatura es: ${total_a_pagar:.2f}") 
