def calcular_colegiatura(costo_materia,num_materias,promedio):

  costo_total = costo_materia * num_materias
  if promedio >=9:
    descuento = costo_total * 0.30
    colegiatura_a_pagar = costo_total - descuento
    return colegiatura_a_pagar
  else:
    impuesto = 0.10 * costo_total
    colegiatura_a_pagar = costo_total + impuesto
    return colegiatura_a_pagar


costo_materia = int(input("Ingrese el costo de la materia: "))
num_materias = int(input("Ingrese el numero de materias: "))
promedio = int(input("Ingrese el promedio: "))




total_a_pagar = calcular_colegiatura(costo_materia,num_materias,promedio)


print(f' el alumno debe pagar {total_a_pagar}')