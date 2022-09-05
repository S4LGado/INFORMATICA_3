#==>  EJERCICIO 12 
""" Un proyectil es lanzado verticalmente hacia arriba, calcule la velocidad inicial que debe tener para 
alcanzar una altura dada. """

h = float (input (" Digite la altura en la cual desea que llegue el proyectil en metros: "))

vo = (2*h*9.82)**(1/2)

print ("La velocidad con la cual debería salir despegado es de: ", vo, " m/s")