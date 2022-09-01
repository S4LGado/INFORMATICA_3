#==>  EJERCICIO 9 
""" El salario mensual de un empleado se calcula teniendo en cuenta el numero de seguros vendidos,
    en donde el precio de cada seguro es de $120000. 
    Para los primeros 20 seguros, la comisión es del 20%.
    Para los siguientes 100 seguros las comisión es del 30%.
    Para los siguientes seguros vendidos. La comisión es de 10%.
    a) Si un empleado vende 435 seguros, ¿cual será su salario?
    b) Para un salario de $10'000.000. ¿Cuántos seguros debe vender?
    c) Si un empleado devenga $15'000.000. ¿Cuantos salarios vendió en promedio al dia? 
       Teniendo en cuenta que solo trabajaba de lunes a jueves """


# literal a

salarioa = 120000*20*1.2 + 120000*100*1.3 + 315*120000*1.1

# literal b

segurosb = (10000000-120000*20*1.2)/(120000*1.3) 

# literal c

segurosc = (15000000-120000*20*1.2)/(120000*1.3)
pdia = segurosc/(4*30)

print("a) su salario es de: ", salarioa)
print("b) debe vender : ",segurosb," seguros")
print("c) debió vender en promedio por dia: ",pdia," seguros")

