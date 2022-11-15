# 15 - 11- 2022

data = list(range(1,1000,2))
nombreArchivo = "DATA.json"
import json

with open("EJERCICIOSENCLASE/13_PersistenciaDatos/" + nombreArchivo ,"w") as file:
    json.dump(data,file)


"""
Almacene la siguiente informacion en un archivo estudiantes.json
   Nombre          Nota1   Nota2  Nota3
Maria Gonzalez       3.1    3.1    1.2 
Camilo Suarez        3.2    4.0    1.1 
Esteban Rodriguez    3.2    4.1    2.2 
Mariana Rosero       5.0    5.0    5.0 
Jose Nuñez           5.0    4.0    2.5 
Esteban Quesada      3.4    4.0    2.6 
Mauricio Velazquez   5.0    4.2    2.1 
Julia Quintero       2.0    2.2    2.1 
Mauricio Lizcano     3.7    4.1    4.7 
Miguel Pineda        1.0    1.1    3.3 
Angie Gomez          4.1    4.7    4.4 
Angelica Lozano      3.1    1.0    2.6 
Camilo Restrepo      5.0    5.0    1.0 

"""

nombres = [
    'Maria Gonzalez    ',
    'Camilo Suarez     ',
    'Esteban Rodriguez ',
    'Mariana Rosero    ',
    'Jose Nuñez        ',
    'Esteban Quesada   ',
    'Mauricio Velazquez',
    'Julia Quintero    ',
    'Mauricio Lizcano  ',
    'Miguel Pineda     ',
    'Angie Gomez       ',
    'Angelica Lozano   ',
    'Camilo Restrepo   '
]

nota1 = [
    3.1,
    3.2,
    3.2,
    5.0,
    5.0,
    3.4,
    5.0,
    2.0,
    3.7,
    1.0,
    4.1,
    3.1,
    5.0
]

nota2 = [
    3.1,
    4.0,
    4.1,
    5.0,
    4.0,
    4.0,
    4.2,
    2.2,
    4.1,
    1.1,
    4.7,
    1.0,
    5.0
]

nota3 = [
    1.2,
    1.1,
    2.2,
    5.0,
    2.5,
    2.6,
    2.1,
    2.1,
    4.7,
    3.3,
    4.4,
    2.6,
    1.0,
]

listatotal = [nombres,nota1,nota2,nota3]

nombreArchivo1 = "prueba1.json" 


with open("EJERCICIOSENCLASE/13_PersistenciaDatos/" + nombreArchivo ,"w") as file:
    json.dump(listatotal,file)
