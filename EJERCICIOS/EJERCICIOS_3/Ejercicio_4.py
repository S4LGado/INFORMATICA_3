""" Ejercicio empleados """
empleados= ["Emplea_1" , "Emplea_2 ", " Emplea_3",  "Emplea_4,",  "Emplea_5",  "Emplea_6",  " Emplea_7",  "Emplea_8",  "Emplea_9",  "Emplea_10",  "Emplea_11",  "Emplea_12 " ,"Emplea_13 " ,"Emplea_14 ", "Emplea_15" , "Emplea_16",  "Emplea_17 ", "Emplea_18",  "Emplea_19",  "Emplea_20",  "Emplea_21" , "Emplea_22" , "Emplea_23 ", "Emplea_24",  "Emplea_25",  "Emplea_26",  "Emplea_27" ]
rendimiento= ["C" ,      "B" ,     "B" ,       "B"   ,     "C" ,     "B" ,     "A" ,       "C"    ,   "B"  ,      "A"  ,      "C"   ,    "B"   ,     "B"    ,    "B"     ,    "B"    ,    "A"    ,   "B"      ,  "A"         ,"A"   ,     "C" ,      "B" ,       "B"   ,     "B"    ,     "B"  ,       "C" ,      "A" , "B"]

cont=0
tamano= len(empleados)
for i in range(0,tamano):
    if rendimiento[i] == "A":
        print(empleados[i], rendimiento[i])
