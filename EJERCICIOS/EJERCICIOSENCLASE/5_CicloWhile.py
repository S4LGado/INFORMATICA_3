"""
Desarrolle un ciclo while infinito
"""
# condicion = True
# 
# while condicion:
#     print("ciclo ejecutado")

"""Cómo protegernos de un ciclo infinito"""
"""
condicion = True
contador = 0
while condicion:
     print("ciclo ejecutado {}".format(contador))
     contador = contador + 1
     if contador == 100: 
        break
"""
"""
Realice un ciclo while con un numero secreto. Cada vez que se ejecuta
un ciclo, el programa pide adivinar el numero, en caso de no ser acertado
se debe mostrar un mensaje diciendo: "Estás atrapado". Y en caso contrario
terminar el ciclo y avisar que el numero es correcto.
"""
#numero_secreto = 999
#numero_usuario = int(input("Ingrese el número secreto: "))
#condicion = (numero_secreto != numero_usuario)
#
#while condicion:
#    print("No es el número correcto")

"""
Realice un ciclo while que imprima los números del 10 al 100, separados por guion(-)
sin salto de linea
10 - 11 - 12 - 13 - ... 100
"""
"""
contador = 10
stringnumeros = ""
while contador <= 100:
        stringnumeros = stringnumeros + str(contador) + "-"
        contador = contador + 1
print (stringnumeros)

"""

# Mostrar los números del 200 al 100 utilizando ciclo while
# Ahora sin salto de linea
"""


while i >= 100:
        print (i, end=" ") # El comando end sirve para que al escribir con print, no haya salto de linea
        i = i - 1
"""

# Mostrar los números del 200 al 100 utilizando ciclo while
# Ahora haga que el salto de linea se haga cada multiplo de 10
"""
contador = 200
while (contador>=100):
        if (str(contador)[-1] in "098765432"):
                print(contador, end=" ")
        else:
                print(contador, end="\n")
        contador = contador - 1

"""

# Pida a un usuario que ingrese numeros, en caso de que asi lo desee.
# De lo numeros calcule cuál es el mayor de los ingresados.
# Si el usuario dese ano ingresar mas numeros el ciclo debe terminar
"""
respuesta = "si"
mayor = -9999999999999
while respuesta == "si":
        respuesta = input ("Desea ingresar un número?: ")
        if respuesta == "si":
                numero = int(input("Ingrese el número: "))
                if numero > mayor:
                        mayor = numero
        else:
                respuesta = "no"
print("El numero mayor es", mayor)
"""

# Otra forma de hacerlo
"""
x = "si" 
lista = []
while x == "si":
        x = input("Desea ingresar un número (si/no): ")
        if x == "si":
                n = int(input("Ingrese el numero: "))
                lista.append(n)
        else:
                x = "no"
print(lista)
print(max(lista))
"""

#Contraseña
"""
contraseña = input("Digite su contraseña: ")
tamaño = len(contraseña)
cont = 0
validez = False
while cont < tamaño:
        if contraseña[cont] in "abcdefghijklmnopqrstuvwxyz":
                validez = True
        if contraseña[cont] in "1234567890":
                validez = True
        if contraseña[cont] in "!#$%&/()=@":
                validez = True
cont = cont + 1 

if validez == False:
        print(" Su cotraseña no es valida")
elif validez == True:
        print("Su contraseña es correcta")
"""