cadena = "MundoCruel"



# Metodos de los String
"""
Retornar caracteres en mayusculas
Retornar caracteres en minusculas
Retornar el numero de veces que se repite un caracter
Retornar si la cadena es alfabetica
Retornar si la cadena es alfanumerica
Retornar si la cadena contiene numeros
Reemplazar una letra por otra

"""

"""
print(cadena.upper()) 
print(cadena.lower())
print(cadena.count("u"))
print(cadena.isalpha())
print(cadena.isalnum())
print(cadena.isnumeric())
print(cadena.replace("u","i"))

"""

"""

Aquí no se altera la cadena principal en este caso "cadena", solo se crea una nueva variable con el cambio deseado

"""

# Indexación de Cadenas

cadena2 = "Mundo Unal"

print (cadena2[0: 10: 2])

# Cadena al revés

print(cadena2[-1::-1])

# Elementos ubicados en las posiciones 3,5 y 7

print(cadena2[2:8:2])

# Elementos hasta la mitad de la cadena

print(cadena2[0:(len(cadena2)//2):1])

# Elementos de la mitad en adelante
print(cadena2[(len(cadena2)//2):len(cadena2):1])

cadena3= "Anita no lava la tina de lunes a viernes"

#Extraer el primer elemento
#Extraer el ultimo elemnto
#Extraer los dos elementos de la mitad
#Extraer la cadena al revés
#Extraer del 10mo al 15avo elementos al revés
#Extraer cada 10mo elemento

"""
Buscar y utilizar métodos para hacer lo siguiente:
Pasar la cadena a mayusculas
Pasar la cadena a minusculas
Reemplazar la palabra Anita y colocar su nombre
Pasar la cadena a formato de títtulo
Contar el número de veces que aparecen las vocales

"""

cadena = 'holamundocruel'
print(cadena [0]) # Extrae el primer elemento 
print(cadena [-1]) # Extrae el ultimo elemento
print(cadena [7]) # Extrae el elemento de la mitad

print(cadena[6]+cadena[7])

# Metodos de las listas

lista = [1,'a',2,3,'b']

lista.append('1000') # Agrega un valor la lista
lista.append(10)
lista.insert(5,10) # Inserta un valor en un indice deseado (indice,valor)
lista.pop(0) # Indica que indice eliminar 
lista.insert(4,'Salgado')

# Son metodos inplace por lo tanto si se printean dan un None

# Eliminar los elementos que no se pueden sumar algebraicamente
# Sumar los elementos restantes afectando lista 2

lista2 = [1,2,'Juan',3,'b','Salgado',10]
lista2.pop(2)
lista2.pop(3)
lista2.pop(3)

"""
Otra forma de hacerlo es: 
for indice in [2,3,3]:
  lista2.pop(i)

"""
# Con Control+Shift+A se puede comentar todo lo seleccionado
#Sumar los elementos sin afectar lista 3
lista3 = [1,2,100,3,'b','Salgado',10,'holamundo',5]
lista3copia = lista3.copy()
lista3copia.pop(4)
lista3copia.pop(4)
lista3copia.pop(5)
lista3copia.sort() # Organiza de menor a mayor
lista3copia.sort(reverse = True) # Organiza de mayor a menor

# Metodo indexado y slicing

listaNueva = [1,2,3,4,5,'hola','cruel','mundo',100]

# Metodo

# Extraer el primer elemento de 2 maneras

print(listaNueva[0],listaNueva[-9])

# Extraer el ultimo elemento de 2 maneras

print(listaNueva[8],listaNueva[-1])

# Extraer el elmento de la mitad de 2 maneras

print(listaNueva[4],listaNueva[-5])

# Slicing

# Extraer cada elemento de dos en dos
print(listaNueva[0:9:2]) # Otra forma de llegar al final es [0::2]
# Extraer hasta la mitad de la cadena
print(listaNueva[0:5:1])
# Extrear desde la mitad de la cadena en adelante
print(listaNueva[5::1])
# Extraer los elementos que son strings
print(listaNueva[5:8])
# Extraer los elementos que son enteros
print(listaNueva[0:5] + [listaNueva[-1]])



