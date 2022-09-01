#==>  EJERCICIO 3 
""" ¿Cuantas veces supera, el area de un cubo, al area de una esfera, si el lado del
cubo es 10 cm. Y el radio de la esfera 2 cm ? """

import math

# Primero se calculan las respectivas areas

Acubo = 6*10*10

Aesfera = 4*(math.pi)*(2*2)

# Se calcula el número de veces que supera

n= Acubo // Aesfera

print ('El área del cubo supera en ', n , ' a la de la esfera')