import interfaz
import logica
print(dir(interfaz)) 
print(interfaz.__doc__) # Muestra la documentacion de un archivo 
print(interfaz.__file__) # Muestra la ubicacion de los archivos

interfaz.separador("-")
interfaz.imprimirNombre("Juan Esteban Salgado")
interfaz.imprimirVariable("Cedula",1000078067)

print(logica.suma3(3,4,6))
print(logica.sumaN(1,2,3,4,5,6))
print(logica.suma2Listas([2,4],[3,1]))

