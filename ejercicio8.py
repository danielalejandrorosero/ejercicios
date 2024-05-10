def registrar_dias(lunes, miercoles, viernes):

  sumar_tiempos = (lunes +miercoles +viernes) / 3
  return sumar_tiempos




lunes = 30
miercoles = 35
viernes = 32


promedio =  registrar_dias(lunes,miercoles,viernes)
print(f'El promedio de tiempo es: ', promedio)