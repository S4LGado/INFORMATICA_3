# Son elementos compuestos por clave : valor
diccionario = {
        'Cristian pachon' : 3.0,
        'Daniel Quintero' : 4.0,
        'Esteban Chavez' : 5.0,
        'Margarita Maria' : 3.5
}

print(diccionario['Cristian pachon']) # Con esto se busca un elemento especifico del diccionario
print(diccionario.get('Juan David gonzales','No existe'))
try:
  print(diccionario['Juan David gonzales']) # Prueba de errores
except:
  print('Esto es un error el programa continua')

# Extraer todas las claves del diccionario

print(diccionario.keys())

# Extraer todos los valores del diccionario

print(diccionario.values())

# Ejercicio recorrer mediante un ciclo for todas las claves 
# del diccionario
keys = []
values = []
for i in diccionario.keys():
  print(i)

# Ejercicio recorrer mediante un ciclo for todos los valores
# del diccionario

for i in diccionario.values():
  print(i)

# Ejercicio imprimir todas las parejas clave : valor con un ciclo for

for i in diccionario.keys():
  print(i,'=',diccionario[i])
# print('{}={}'.format(i,diccionario[i])) otra forma en la que se quita el espacio entre la clave y el valor

# otra forma utilizando el metodo .items

for pareja in diccionario.items():
  print(pareja[0]+'='+str(pareja[1]))

# otra forma mas elegante es definiendo al mismo tiempo dos elementos de la lista

for key,value in diccionario.items(): # Se le llama desempaquetado
  print(key + '=' + str(value)) 

# Como cambiar los valores del diccionario

diccionario['Cristian pachon'] = 5.0

# cambiar todas las notas a 0.0

for notas in diccionario:
  diccionario[notas] = 0.0

# si es hombre poner 0.0 y si es mujer poner 5.0

for key in diccionario.keys():
  if key[-1] == 'a':
    diccionario[i] = 5.0
  else:
    diccionario[i] = 0.0

# haga una copia de diccionario y cambie las notas a 5.0

diccionarioCopia = diccionario.copy()

for nombre in diccionarioCopia.keys():
  diccionarioCopia[nombre] = 5.0

# Como eliminar un par clave:valor del diccionario
del diccionario['Cristian pachon']

# Ejercicio cambiar la clave Margarita Maria
# a Margarita rosa

valor = diccionario['Margarita Maria']
del diccionario['Margarita Maria']
diccionario ['Margarita Rosa'] = valor

""" 
Nombre                         Materias
                    Cuantica Etica Deportes Lenguas
Juan Gutierrez        2.0     5.0     1.3     3.2
Maria Snowden         3.1     4.9     2.2     1.1
Pedro Gonzalez        5.0     3.8     3.1     4.1
Angelica Lozano       2.1     2.7     4.1     3.2
Pablo Iglesias        3.2     1.6     5.0     1.2
Mariana Pajon         2.2     2.5     4.9     3.3
Esteban Loaiza        2.1     3.4     3.8     4.3
Daniela Pineda        5.0     4.3     2.7     1.2
Esteban Vazco         3.1     5.0     1.6     3.2
Enilse Lopez          5.0     2.2     2.5     5.0
Cristian Playonero    0.5     1.1     3.4     3.2
 """

Nombres = {
'Juan Gutierrez' :     {'Cuantica': 2.0   , "Etica": 5.0 },   
'Maria Snowden' :      {'Cuantica': 3.1   , "Etica": 4.0},
'Pedro Gonzalez' :     {'Cuantica': 5.0  , "Etica": 3.8 },
'Angelica Lozano' :    {'Cuantica': 2.1  , "Etica": 2.7},
'Pablo Iglesias' :     {'Cuantica': 3.2  , "Etica": 1.6},
'Mariana Pajon' :      {'Cuantica': 2.2  , "Etica": 2.5},
'Esteban Loaiza' :     {'Cuantica': 2.1  , "Etica": 3.4},
'Daniela Pineda' :     {'Cuantica': 5.0  , "Etica": 4.3},
'Esteban Vazco' :      {'Cuantica': 3.1  , "Etica": 5.0},
'Enilse Lopez' :       {'Cuantica': 5.0 , "Etica":  2.2},
'Cristian Playonero' : {'Cuantica': 0.5  , "Etica": 1.1}
}

print(Nombres['Maria Snowden']['Cuantica'])