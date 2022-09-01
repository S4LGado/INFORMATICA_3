#==>  EJERCICIO 4 
""" Realice un código, que permita la conversión de millas a km y km a millas """

print ("Si desea convertir de m --> Km marque 1")
print ("Si desea convertir de Km --> m marque 2")

n = int(input ("Digite su opción: "))

# Se utiliza el condicional if para tratar de crear una especie de menú

if n == 1:
    m = float (input("Digite las millas : "))
    km = m*1.609
    print ("Esta cantidad de millas en Kilómetros equivalen a: ",km)

if n == 2:
    
    km= float (input("Digite los kilómetros : "))
    m = km/1.609
    print ("Esta cantidad de Kilómetros en millas equivalen a: ",m)

