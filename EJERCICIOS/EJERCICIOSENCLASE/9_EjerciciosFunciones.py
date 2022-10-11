def saludarEstudiante(nombre): #Definicion de la funcion
    saludo = "hola" + " " + nombre
    return saludo

saludoRecibido = saludarEstudiante(Juan Esteban Salgado)
print(saludoRecibido) # Esto si aparece en pantalla

"""
1) Desarrollar una funcion que reciba dos numeros y 
devuelva la suma de ambos
"""

def suma(a,b):
  resultadoSuma = a + b
  return resultadoSuma

"""
2) Desarrollar una funcion que reciba dos listas y devuelva una nueva lista,
que sume elemento a elemento
"""

def sumaListas(c,d):
  resultadoSumaListas = []
  for i in c:
    valor = i + d[c.index(i)]
    resultadoSumaListas.append(valor)
  return resultadoSumaListas 

"""
3) Desarrollar una funcion que no reciba parametros
y que no tome valores, pero que sirva para imprimir un mensaje
de 3 lineas
"""

def mensaje3Lineas():
  Lineas = "\n \n \n"
  return Lineas

"""
4) Desarrollar una funcion, que reciba un diccionario 
de calificaiones (nombre = calificacion)
y retorne el promedio
"""

def promedioCalificaciones(a):
  promedio = sum(a.values())/len(a.values())
  return promedio

"""
5) Producto de numeros
"""

def productoDeNumeros(*numeros): # Ese simbolo sirve para desempaquetar
  resultado = 1
  for numero in numeros:
    resultado = resultado*numero
    return resultado
