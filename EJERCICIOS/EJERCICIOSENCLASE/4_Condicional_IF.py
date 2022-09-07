#06-09-2022

# Ejercicio 1
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
# Ejercicio 2
"""
Realice un programa que calcule el mayor de tres numeros
"""
"""
a = float(input("Digite el numero 1: "))
b = float(input("Digite el numero 2: "))
c = float(input("Digite el numero 3: "))

if a >= b and a >= c:
    mayor = a
elif b >= a and b >= c:
    mayor = b
elif c >= a and c >= b:
    mayor = c

print ("El mayor numero entre los ingresados es: ",mayor)

"""
# Ejercicio 3
"""

Salario base = 1000000

Realice un programa que calcule el salario de un vendedor
de seguros, teniendo en cuenta las siguientes condiciones =>

=> ventas => entre [5, 20] seguros =>
    aumento del 20% sobre la base
=> ventas => entre [21, 50] seguros =>
    aumento del 30% sobre la base
=> ventas => entre [51, infinito] seguros =>
    aumento del 35% sobre la base        

"""
"""
salario = 1000000
ventas=float(input("Digite la cantidad de ventas que realizc en este mes:"))

if 20 >= ventas >= 5:
    salario = 1000000*1.2
elif 50 >= ventas >= 21:
    salario = 1000000*1.3
elif ventas >= 51:
    salario = 1000000*1.35

print ("Segun sus ventas el salario que devenga en este mes es de: ",salario)
"""

# Ejercicio 4

"""
Una contrasena de un programa, debe incluir:

* Contrasena contenga mayusculas
* Contrasena contenga minusculas
* Contenga numeros
* Caracteres especiales
* Por lo menos 8 caracteres en total

Determine si al ingresar una contrasena, se cumple con todas las condiciones.

"""
"""
condicion1 = <Contenga mayusculas>
condicion2 = <Contenga minusculas>
condicion3 = <Contenga numeros>
condicion4 = <Caracteres especiales>
condicion5 = <Por lo menos 8 caracteres en total>

if condicion1 and condicion2 and condicion3 and condicion4 and condicion5:
    print ("Es valido").

elif 
    print ("No es valido")"""