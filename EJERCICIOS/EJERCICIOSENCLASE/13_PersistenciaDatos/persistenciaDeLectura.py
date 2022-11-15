# 15 - 11 - 2022

# ---------- Lectura archivos Json ------------

"""
Leer archivo DATA.json
y luego calcular la media de los valores
"""

archivo = "DATA.json"
ruta = "EJERCICIOS/13_PersistenciaDatos/" + archivo
opcion = 'r' #Lectura

with open(ruta,opcion) as file:
    data = json.load(file)

print('media => ', sum(data)/len(data))

"""
Leer el archivo estudiantes.json
calcular el promedio de cada estudiante
"""

archivo1 = "estudiantes.json"
ruta = "EJERCICIOS/13_PersistenciaDatos/" + archivo1
opcion = 'r' #Lectura

with open(ruta,opcion) as file:
    data1 = json.load(file)

promedio = []
promedioEstudiantes = {}
for i in range (0,len(data1[1])):
    promedio.append(round((data1[1][i]+data1[2][i]+data1[3][i])/3,2))

for i in data[0]:
    promedioEstudiantes[i] = promedio[i]