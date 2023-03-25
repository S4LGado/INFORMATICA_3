nombre_completo = "Juan Esteban Salgado" 

# EJERCICIO 1

def esMayorDeEdad(edad):
    mayorDeEdad = False
    if edad >= 18:
        mayorDeEdad = True
    return mayorDeEdad

def sumadeDigitos(num):
    num = str(num)
    sumadeDigitos = 0
    for i in num:
        sumadeDigitos += int(i)
    return sumadeDigitos

def tieneVocales(palabra):
    tieneVocales = False
    for i in palabra:
        if i in ["a","e","i","o","u","A","E","I","O","U"]: 
            tieneVocales= True
    return tieneVocales

def esPrimo(num):
    esPrimo = True
    for i in range (2,num):
        if num%i == 0:
            esPrimo = False
    return esPrimo

funciones = [esMayorDeEdad, sumadeDigitos, tieneVocales, esPrimo]

# EJERCICIO 2

trayectos = {
"Mariana" :      ["Si","No","Si","No","No","No","No","Si","No","No"],
"Sofia"   :      ["Si","No","No","Si","Si","Si","No","No","Si","No"],
"Camila"  :      ["Si","No","Si","No","Si","No","No","No","No","No"],
"Maria"   :      ["Si","Si","Si","No","No","No","No","Si","No","No"],
"Juan"    :      ["Si","Si","Si","Si","No","Si","No","Si","No","No"],
"Angie"   :      ["Si","No","Si","No","No","Si","No","Si","No","No"],
"Esteban" :      ["Si","No","No","Si","Si","No","No","No","Si","No"],
"Jose"    :      ["Si","No","Si","Si","No","Si","No","Si","Si","No"],
"Gisell"  :      ["Si","Si","No","Si","No","Si","No","Si","No","No"],
"Cristian":      ["Si","Si","Si","No","No","Si","Si","Si","No","No"]
}

diccionarioPagos = {
"Mariana" : 0,
"Sofia"   : 0,
"Camila"  : 0,
"Maria"   : 0,
"Juan"    : 0,
"Angie"   : 0,
"Esteban" : 0,
"Jose"    : 0,
"Gisell"  : 0,
"Cristian": 0,
}


for j in range(0,10):
    contador = 0
    for i in trayectos.keys():
        if trayectos[i][j] == "Si":
            contador += 1
    for i in trayectos.keys():
        if trayectos[i][j] == "Si":
            diccionarioPagos[i] += 15000/contador 
    if contador == 0:
        for j in trayectos.keys():
            diccionarioPagos[j] += 10000/10

for i in diccionarioPagos.keys():
    diccionarioPagos[i] = round(diccionarioPagos[i],2)
        

# EJERCICIO 3

productos = [
  [38000,3],
  [55500,5],
  [71000,4],  
  [29500,2],
  [25000,7],
  [80500,5],
  [95000,2],
]
      
empleados = {
     "001":[40,20,22,30,2 ,20,3 ],   
     "002":[13,31,14,32,15,20,11],   
     "010":[12,24,32,40,9 ,50,13],   
     "020":[22,42,12,33,24,32,23],   
     "021":[19,51,21,25,10,14,2 ],   
     "022":[35,22,31,51,21,15,11],   
     "023":[39,21,36,22,32,32,15],   
     "024":[43,22,33,41,21,31,36],   
     "025":[33,33,31,20,42,42,35],   
     "031":[37,22,47,5 ,28,31,32],   
     "032":[41,24,38,33,21,31,16],   
     "033":[39,21,18,32,37,22,12],   
     "041":[33,33,31,21,21,39,25],   
     "042":[15,25,39,20,48,30,32],   
     "043":[37,27,32,29,28,35,16],   
     "121":[39,24,12,31,21,32,13],   
     "122":[13,31,31,50,22,30,21],   
     "123":[31,23,35,35,39,19,19],   
     "351":[35,26,36,39,27,32,16],   
     "352":[25,25,31,21,21,37,15],   
     "353":[37,23,34,35,32,20,49],   
     "368":[25,31,14,29,39,37,16],   
     "369":[37,26,31,31,27,32,41],   
     "461":[21,40,42,23,11,15,19],   
     "466":[31,27,31,39,21,32,25],   
     "469":[35,38,32,19,29,50,16]   
}
salarios = {
"001": 1200000, 
"002": 1200000,
"010": 1200000,
"020": 1200000,
"021": 1200000,
"022": 1200000,
"023": 1200000,
"024": 1200000,
"025": 1200000,
"031": 1200000,
"032": 1200000,
"033": 1200000,
"041": 1200000,
"042": 1200000,
"043": 1200000,
"121": 1200000,
"122": 1200000,
"123": 1200000,
"351": 1200000,
"352": 1200000,
"353": 1200000,
"368": 1200000,
"369": 1200000,
"461": 1200000,
"466": 1200000,
"469": 1200000
}
codigosAltosSalarios =[]

for i in empleados.keys():
    for j in range(0,7):
        salarios[i] += empleados[i][j]*productos[j][1]*0.01*productos[j][2]

mayor = 0
codigomayor = ""
for j in range(0,3):
  for i in salarios.keys():
      if salarios[i] > mayor:
        mayor = salarios[i]
        codigomayor = i
  salarios[codigomayor]=0
  mayor = 0
  codigosAltosSalarios.append(codigomayor)

# EJERCICIO 4

puntos = {
"P1" :(5, 2, 3),     
"P2" :(4, 1, 3),     
"P3" :(2.5, 1, 0),     
"P4" :(0.5, 0.5, 2),     
"P5" :(1, 2, 1),     
"P6" :(6, 2, 1),      
"P7" :(3, 2, 0.5),    
"P8" :(2, 6, 1),    
"P9" :(0, 0, 0),    
"P10":(2, 0, 0.5),       
"P11" :(2, 2, 3),
"P12" :(2, 3, 4),
"P13" :(1, 1, 3),
"P14" :(4, 4, 4),
"P15" :(5, 5, 1),
"P16" :(1, 0.5, 1),
"P17" :(3, 4, 5),
"P18" :(3, 1, 2),
"P19" :(3, 9, 1),
"P20" :(0.5, 0.5,6)
}

menordiferencia = float(100000)
parCercano = ""
puntoA,puntoB = "" , ""
for i in puntos.keys():
    for j in puntos.keys():
        if i != j:
            diferencia = ((puntos[i][0] - puntos[j][0])**2 + (puntos[i][1] - puntos[j][1])**2 + (puntos[i][2] - puntos[j][2])**2)**(1/2)
            if diferencia < menordiferencia:
              menordiferencia = diferencia
              puntoA= i
              puntoB= j
          
parCercano = str(puntoA+"-"+puntoB)

# EJERCICIO 5
precios ={
"A001":31000,
"A011":25000,
"A032":43000,
"A125":55000,
"B001":10000,
"B005":20000,
"P009":30000,
"P019":49000,
"R001":60000,
"W307":90000,
"Z052":35000,
"Z025":27000,
"Z278":65000
}

registros = ["P009-21Unidades", "B005-19Unidades", "B001-19Unidades", "P009-31Unidades", "B005-22Unidades", "W307-15Unidades", "A011-31Unidades", "P019-18Unidades", "A011-20Unidades", "R001-20Unidades", "P019-19Unidades", "A001-12Unidades", "A125-20Unidades", "R001-31Unidades", "Z052-52Unidades", "W307-31Unidades", "Z025-42Unidades", "Z052-10Unidades", "Z278-30Unidades", "Z025-24Unidades", "Z278-21Unidades", "A001-31unidades", "A032-52Unidades", "B001-29Unidades", "A125-15Unidades", "A032-22Unidades" ]
dinero_total= 0

def ventasEmpresa(registros):
    dinero_total = 0
    for i in registros:
        dinero_total += precios[i[0:4]]*float(i[5:7])
    return dinero_total

