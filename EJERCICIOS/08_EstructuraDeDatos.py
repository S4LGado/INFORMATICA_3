import numpy
import pandas

#Ejericio 1 ===============>
"""
Crear un solo arreglo numpy con la siguiente informacion 
de los estudiantes que usan el servicio de taxi
                            IDA                             
            LUNES   MARTES  MIERCOLES   JUEVES  VIERNES     
JUAN          Si        Si        Si      Si      No        
CAMILA        Si        No        Si      No      Si        
JOSE          Si        No        Si      Si      No        
MARIA         Si        Si        Si      No      No        
ESTEBAN       Si        No        No      Si      Si        
ANGIE         Si        No        Si      No      No        
"""

data =[['1','1','1','1','0'],
       ['1','0','1','0','1'],
       ['1','0','1','1','0'],
       ['1','1','1','0','0'],
       ['1','0','0','1','1']
       ['1','0','1','0','0']]

usoDeTaxi = numpy.array(data)
print(usoDeTaxi,usoDeTaxi.dtype)

#Ejercicio 2 ===============>

"""
Crear una serie con informacion del rendimiento de los 'empleados', en una empresa =>
--------------  Emplea_1  Emplea_2  Emplea_3  Emplea_4  Emplea_5  Emplea_6  Emplea_7  Emplea_8  Emplea_9  Emplea_10  Emplea_11  Emplea_12  Emplea_13  Emplea_14  Emplea_15  Emplea_16  Emplea_17  Emplea_18  Emplea_19  Emplea_20  Emplea_21  Emplea_22  Emplea_23  Emplea_24  Emplea_25  Emplea_26  Emplea_27 
Rendimiento --    "C"       "B"      "B"        "B"        "C"      "B"      "A"        "C"       "B"        "A"        "C"       "B"        "B"        "B"         "B"        "A"       "B"        "A"         "A"        "C"       "B"        "B"        "B"         "B"         "C"       "A"       "C"   """

indices = ['Emplea_1 ', 'Emplea_2 ', 'Emplea_3 ', 'Emplea_4 ', 'Emplea_5 ', 'Emplea_6 ', 'Emplea_7 ', 'Emplea_8 ', 'Emplea_9 ', 'Emplea_10',  'Emplea_11',  'Emplea_12',  'Emplea_13',  'Emplea_14',  'Emplea_15',  'Emplea_16',  'Emplea_17',  'Emplea_18',  'Emplea_19',  'Emplea_20',  'Emplea_21',  'Emplea_22',  'Emplea_23',  'Emplea_24',  'Emplea_25',  'Emplea_26',  'Emplea_27']
datos = [3, 2,      2,        2,        3,      2,      1,        3,       2,        1,        3,       2,        2,        2,         2,        1,       2,        1,         1,        3,       2,        2,        2,         2,         3,       1,       3 ]

Rendimiento = pandas.series(data= datos, index = indices)

#Ejercicio 3 ===============>
"""
Crear un data frame con los empleados de una empresa:
Cod   Nombre               Cargo          Salario   
0001   Cristian Pachon     Ingeniero      $ 3.200.000
0002   Daniela Pineda      Programador    $ 4.300.000
0003   Esteban Murcia      Programador    $ 4.600.000
0004   Jose Guzman         Ingeniero      $ 3.900.000
0005   Camilo Rodriguez    Ensamblador    $ 1.200.000
0006   Mariana Londoño     Ensamblador    $ 1.100.000
0007   Estefania Muños     Ensamblador    $ 1.700.000
0008   Cristian Rodriguez  Ingeniero      $ 3.100.000
0009   Natalia Alzate      Ensamblador    $ 2.200.000
0010   Juan Sanabria       Diseñador      $ 5.100.000
0011   Juanita Calderon    Ensamblador    $ 1.300.000
0012   Laura Quintero      Administrador  $ 2.500.000
0013   Viviana Quesada     Guardia        $ 1.500.000
"""

columnas = ['Nombre','Cargo','Salario','experiencia']
indices = [
'0001',
'0002',
'0003',
'0004',
'0005',
'0006',
'0007',
'0008',
'0009',
'0010',
'0011',
'0012',
'0013'
]

datos = [
['Cristian Pachon   ' , 'Ingeniero    '  ,3200000,8]
['Daniela Pineda    ' , 'Programador  '  ,4300000,9]
['Esteban Murcia    ' , 'Programador  '  ,4600000,10]
['Jose Guzman       ' , 'Ingeniero    '  ,3900000,8]
['Camilo Rodriguez  ' , 'Ensamblador  '  ,1200000,2]
['Mariana Londoño   ' , 'Ensamblador  '  ,1100000,1]
['Estefania Muños   ' , 'Ensamblador  '  ,1700000,5]
['Cristian Rodriguez' , 'Ingeniero    '  ,3100000,8]
['Natalia Alzate    ' , 'Ensamblador  '  ,2200000,6]
['Juan Sanabria     ' , 'Diseñador    '  ,5100000,11]
['Juanita Calderon  ' , 'Ensamblador  '  ,1300000,4]
['Laura Quintero    ' , 'Administrador'  ,2500000,7]
['Viviana Quesada   ' , 'Guardia      '  ,1500000,3]]

Empleados = pandas.DataFrame(datos,indices,columnas)

      
"""
Graficar la dispersion => Años de experiencia vs salario
Graficar el histograma => salario
graficar el histograma => Años de experiencia
graficar el diagrama de barras => cargo vs salario promedio
"""

# Graficar la dispersion => Años de experiencia vs salario

import matplotlib.pyplot as plt

x = dataFrameEmpresa["Años_experiencia"].values
y = dataFrameEmpresa["Salario"].values
plt.figure()
plt.plot(x,y,"or",label = "Dispersion") #Se agrega el "or" para que se vean solo los puntos de dispersion
plt.title(r"$Años\ de\ experiencia\ vs\ Salario$") #Este arreglo se hace para obtener letra cursiva
plt.xlabel(r"$Años$")
plt.ylabel(r"$Salario$")
plt.grid()
plt.legend()
plt.show()


#Graficar el histograma => salario
x = dataFrameEmpresa["Salario"].values
plt.figure()
plt.hist(x,bins = 5 , density = 10)
plt.title(r"$Histograma$")
plt.xlabel(r"$Salarios$")
plt.ylabel(r"$Frecuencias$")
plt.show()
plt.savefig('figura2.png') #Se hace para guardar la imagen cada que se ejecute el programa

#Graficar el histograma => Años de experiencia
x = dataFrameEmpresa["Años_experiencia"].values
plt.figure()
plt.hist(x,bins = 5 , density = 10, color = "#ff1111") # Aqui se puede cambiar el color
plt.title(r"$Histograma$")
plt.xlabel(r"$Años_experiencia$")
plt.ylabel(r"$Frecuencias$")
plt.show()

#  graficar el diagrama de barras => cargo vs salario promedio
print(dataFrameEmpresa)
print(dataFrameEmpresa[["Cargo","Salario"]].groupby(["Cargo"]).mean()) # Es necesario colocar doble [[]] ya que de lo contrario va a entregar una serie
