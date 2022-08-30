""" Dada una cantidad de segundos, realice un algoritmo que los convierta a unidades horas,minutos
mostrando en pantalla en formato "horas:minutos"  """

# Definimos los segundos

segundos = int(input ("Digite la cantidad de segundos: "))

# Le restamos a las horas con decimales su parte entera para quedarnos con los decimales
# Estos decimales se multiplican por 60 y son los minutos

horas = segundos // 3600
minutos = int(((segundos/ 3600)- horas)*60)

print ("Según los segundos ingresados la hora es ", horas, " : ", minutos)