#==>  EJERCICIO 2
""" ¿Qué radio debe tener una esfera, para que su volumen sea el mismo al de un cubo de lado 5 cm? """
# se importa la libreria math para poder utilizar pi

import math

# Se calcula el volumen del cubo

Vcubo = (5)**3

# Se despeja el radio de la fórmula de la esfera

radio = ((3*Vcubo)/(4*(math.pi)))**(1/3)

print ("A partir del volumen del cubo de 5 cm de lado, el radio de la respectiva esfera con el mismo volumen debe ser de: ", radio)