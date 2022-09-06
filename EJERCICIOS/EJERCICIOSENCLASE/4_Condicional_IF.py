#06-09-2022

"""
Pida a un usuario su nombre y su edad. Determine si es mayor de edad,
y muestre un mensaje en pantalla diciendo:
<NOMBRE>, usted es mayor/menor de edad:
"""
"""
nombre = input("INgrese su nombre: ")
edad = int(input("Ingrese la edad: "))

if edad >= 18:
    print(nombre, "{}, usted es mayor de edad", format(nombre))
elif 0 < edad < 18:
    print(nombre, "{}, usted es menor de edad", format(nombre))    
"""

"""
Realice un programa que calcule el mayor de tres numeros
"""

a = float(input("Digite el numero 1: "))
b = float(input("Digite el numero 2: "))
c = float(input("Digite el numero 3: "))

if a > b and a > c:
    mayor = a
elif b > a and b > c:
    mayor = b
elif c > a and c > b:
    mayor = c

print ("El mayor numero entre los ingresados es: ",mayor)