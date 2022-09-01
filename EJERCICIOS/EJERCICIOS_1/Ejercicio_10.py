#==>  EJERCICIO 10 
""" El salario de un empleado de una empresa se calcula, utilizando como base el 
salario minimo, más un apoyo del 10% en transporte, y uno de 5% por gastos varios.
Además se paga una comisión de acuerdo al numero de ventas de los siguientes productos:
           
            precio_unidad  comisión
* Zapatos:    $ 50 000        5%
* Tenis:      $ 70 000        4%  
* Camizas:    $ 40 000        6%
* Corbatas:   $ 25 000        7%
* Pantalon:   $ 35 000        5%
* Blusas:     $ 80 000        3%
* Vestidos:   $ 95 000        2%
* Medias:     $ 10 000        8%
a) Realice un algoritmo que calcule el salario del empleado teniendo en cuenta el numero de ventas realizadas 
b) Uno de los directivos, quiere que la comisión de cada uno de los productos no supere los $2000
   ¿Qué productos deben cambiar en su porcentaje de comision?
c) Otro directivo desea que la comisión de cada producto se fije en $1900, 
   ¿en cuanto se deben fijar las comisiones de los productos"""

# Literal a
zapatos =  int(input( "Digite la cantidad de Zapatos: "))
tenis =    int(input( "Digite la cantidad de Tenis: ")) 
camisas =  int(input( "Digite la cantidad de Camisas: "))
corbatas = int(input( "Digite la cantidad de Corbatas: "))
pantalon = int(input( "Digite la cantidad de Pantalones: "))
blusas =   int(input( "Digite la cantidad de Blusas: "))
vestidos = int(input( "Digite la cantidad de Vestidos: "))
medias =   int(input( "Digite la cantidad de Medias: "))

Czapatos = 50000*0.05
Ctenis = 70000*0.04
Ccamisas = 40000*0.06
Ccorbatas = 25000*0.07
Cpantalon = 35000*0.05
Cblusas = 80000*0.05
Cvestidos = 95000*0.05
Cmedias = 10000*0.05

salario = 1117174*1.15 + (zapatos * Czapatos) + (tenis * Ctenis) + (camisas* Ccamisas) + (corbatas * Ccorbatas) + (pantalon * Cpantalon) + (blusas * Cblusas) + (vestidos * Cvestidos) + (medias * Cmedias)

print (" El salario que gana un empleado es de: ", salario)

# Literal b

if Czapatos > 2000:
    rint ("los zapatos deben cambiar su comisión")
if Ctenis > 2000:
    print ("los tenis deben cambiar su comisión")
if Ccamisas> 2000:
    print ("las camisas deben cambiar su comisión")
if Ccorbatas > 2000:
    print ("las corbatas deben cambiar su comisión")
if Cpantalon> 2000:
    print ("los pantalones deben cambiar su comisión")
if Cblusas > 2000:
    print ("las blusas deben cambiar su comisión")
if Cvestidos > 2000:
    print ("los vestidos deben cambiar su comisión")
if Cmedias > 2000:
    print ("las medias deben cambiar su comisión")