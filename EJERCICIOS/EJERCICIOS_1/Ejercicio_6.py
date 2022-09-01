#==>  EJERCICIO 6 
""" La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas, 
con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 3 calificaciones definidas.
Realice un algoritmo que calcule la nota necesaria de la última nota para pasar la materia. """

a = float(input ("ingrese la primer nota: "))
b = float(input ("ingrese la segunda nota: "))
c = float(input ("ingrese la tercer nota: "))

sparcial = a*0.15 + b*0.25 + c*0.20
e = 5.0 - sparcial
d = e /0.4

if sparcial >= 3.0:
    print("Con sacar 0.0 en la nota ya pasa")

if e < 3.0 and d<=5:
    print("Necesita sacar :",d," para pasar la materia")

if e < 3.0 and d>5:
    print("Ya no pasa la materia")