cadena = "HolaMundoCruel"
lista = [1,2,30,100,50,-20]
print("-Recorrido de una cadena-")
for caracter in cadena :
    print(caracter,end="--") #Escribe cada caracter de la cadena por separado
print ("\n-Recorrido de una lista")
for i in lista: 
    print(i, end="--")

"""
Recorrer los números del 1 al 10 utilizando diferentes iterables (por lo menos 4)
sin necesidad de definirlos en una variable
"""

#forma 1
print ("\n")
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i, end="   ")

#forma 2
print ("\n")
for i in range(1,11):
    print(i, end="   ")

#forma 3
print ("\n")
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i, end="   ")

#forma 4
print ("\n")
for i in "12345678910":
    print(i, end="   ")

"""
Numeros pares del 0  al 20
"""
print ("\n")
for i in range (0,21,2):
    print (i, end=" ")

"""
Numeros multiplos de 4 desde el 5 hasta el 30

"""
for i in range (8,30,4):
    print (i, end="   ")
