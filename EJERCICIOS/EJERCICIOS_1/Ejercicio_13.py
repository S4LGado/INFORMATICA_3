#==>  EJERCICIO 13 
""" Un proyectil es lanzado siguiendo una trayectoria parabólica, calcule el ángulo y la velocidad inicial
que debe tener para alcanzar una distancia horizontal y vertical dada. """

import math

y = float (input (" Digite la altura en la cual desea que llegue el proyectil en metros: "))
x = float (input (" Digite el alcance máximo al cual desea que llegue el proyectil en metros: "))

a = math.atan(((4*y)/x))*180/(math.pi)
v = (2*y*9.8/(math.sin(a*math.pi/180))**2)**(1/2)

print ("La velocidad a la que debe salir es de: ",v, " m/s y con un ángulo de: ",a," grados")