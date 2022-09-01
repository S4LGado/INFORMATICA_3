#==>  EJERCICIO 5 
""" Dadas las coordenadas P1(5,4,5) y P2(0,10,9).
Realice un codigo que determine la distancia entre ambos puntos """

# Primero definimos los vectores 

p1 = [5, 4, 5]

p2 = [0, 10, 9]

# Se resta el primer vector del segundo

a = 5 - 0
b = 4 - 10
c = 5 - 9

D = (a**2 + b**2 + c**2)**(1/2)

print ("La longitud del vector con puntos p1 (5 4 5) y p2 (0 10 9) es de: ",D)

