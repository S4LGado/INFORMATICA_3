#==>  EJERCICIO 7 
""" La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas,
 con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 2 calificaciones definidas.
Realice un algoritmo que calcule la nota necesaria de las dos últimas notas para pasar la materia. """

a = float(input ("ingrese la primer nota: "))
b = float(input ("ingrese la segunda nota: "))

sparcial = a*0.15 + b*0.25 
d = (5 - sparcial)/0.4

if sparcial >= 3.0:
    print("Con sacar 0.0 en la nota ya pasa")

if sparcial < 3.0 and d<=5:
    print("Necesita sacar :",d," en las dos notas para pasar la materia")

if sparcial <3.0 and d>5:
    print("Ya no pasa la materia")