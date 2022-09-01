""" Funciones Integradas """

""" ---- Función Input y Print ---- """
# a = input  ("ingrese su nombre: ") # Interrumpe la ejecución del código hasta que se almacene el valor

# Realice un algoritmo que solicite la edad y que muestre por pantalla si es o no mayor de edad

"""Edad = int(input("Digite su edad: "))
if Edad >= 18:
 print ("Es mayor de edad")
if Edad < 18: 
 print ("Es menor de edad")"""

#Solicite una clave y muestre por pantalla si es correcta o incorrecta. (Clave ==> 9876)

"""clave = int (input("ingrese la clave: "))
print ((clave==9876 and "La clave correcta") or "La clave es incorrecta")"""

""" ---- Función Format ---- """

"""numero = 192.593
formato_cientifico = format (numero, "e")
print (formato_cientifico)

numero1 = 192.593
formato_cientifico1 = format (numero1, ".2e") # Aquí el .2e denota la cantidad de decimales que queremos mostrar
print (formato_cientifico1)

numero2 = 12.95637
formato_flotante = format (numero2, ".2f") # Si aproxima
print (formato_flotante)"""

# Ejercicios de práctica función format
    #    a) 0.52941 , 2.389

"""numero1 = 0.52941

print(format (numero1, ".0f"))
print(format (numero1, ".2f"))
print(format (numero1, ".5f"))
print(format (numero1, ".1e"))
print(format (numero1, ".2e"))

numero2 = 2.389

print(format (numero2, ".0f"))
print(format (numero2, ".2f"))
print(format (numero2, ".5f"))
print(format (numero2, ".1e"))
print(format (numero2, ".2e"))"""

"""cadena = "hola mundo"
formato_centrado = format(cadena, "^50")
formato_derecha = format(cadena, ">50")
formato_izquierda = format(cadena, "<50")

print  ("formato centrado ==> \n", formato_centrado) 
print  ("formato derecha ==> \n", formato_derecha) # El comando \n es para que lo que imprima lo muestre en otro renglon
print  ("formato izquierda ==> \n", formato_izquierda)"""

""" ---- Funciones de conversión ---- """

# Convertir a binario, octal y hexadecimal
"""
decimal = 9
conversion_binario = bin(decimal)
conversion_octal = oct(decimal)
conversion_hex = hex(decimal)

print(conversion_binario)
print(conversion_octal)
print(conversion_hex ) """

# ¿ Cómo hacer lo contrario ?
"""
bin, oct, hex = "1100110", "146", "66"

print (" bin a decimal: ", int(bin,2))
print (" octal a decimal: ", int (oct,8))
print ("hexadecimal a decimal: ", int(hex,16)) """

""" ---- Funciones de Ayuda ---- """

# Función dir
"""
cadena = "holamundo"
lista = [1,2,3]
entero = 10

print("\n funcionalidades para cadena ==> \n\n", dir(cadena))
print("\n funcionalidades para lista ==> \n\n", dir(lista))
print("\n funcionalidades para entero ==> \n\n", dir(entero))"""

""" ---- Funciones para Secuencia ---- """
"""
print ("\n\n Funciones para secuencias ===>")

secuencia = range(1,11,1) #No toma el último valor
print (list(secuencia))
"""
# numeros del 20 al 29
"""
secuencia1 = range (20,30,1) 
print (list(secuencia1))
"""
# numeros -10 al 10 con salto 2
"""
secuencia2 = range (-10,11,2) 
print (list(secuencia2))
"""
# números mútiplos de 3 desde el -10 hasta el 5
"""
secuencia3 = range (-9,6,3) 
print (list(secuencia3))
"""
# números del 10 al 0
"""
secuencia4 = range (10,-1,-1) 
print (list(secuencia4))
"""
# números múltiplos de 3 y 5 del 1 al 1000. Al revés
"""
secuencia5 = range (0,1001,15) 
print (list(secuencia5))

secuencia6 = range (990,1,-15) 
print (list(secuencia6))
"""

#Listas

secuencia7 = range(1,10000,3)
lista = [1,2,3,4,5,8,8,9]

print("Tamaño de secuencia", len(secuencia7))
print("Tamaño de lista", len(lista))

print("Mínimo de secuencia", min(secuencia7))
print("Mínimo de lista", min(lista))

print("Máximo de secuencia", max(secuencia7))
print("Máximo de listaa", max(lista))

print("Revertir secuencia", list(reversed(secuencia7)))
print("Revertir lista", list(reversed(lista)))