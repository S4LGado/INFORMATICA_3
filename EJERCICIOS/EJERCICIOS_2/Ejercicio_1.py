#====================== EJERCICIOS FUNCIONES INTEGRADAS ====================
#==> Ejercicio 1 
"""   (Intente no utilizar la sentencia if)
      a) Pedir al usuario que ingrese su edad, luego imprimir en pantalla si es mayor o menor de edad
      b) Pedir al usuario que ingrese su salario, luego imprimir si su salario es alto o bajo, (salario alto > $ 5000000)
      c) Pedir al usuario que ingrese 3 notas, luego avisar si aprueba o reprueba la materia
"""   
# literal a

e = int (input(" Digite su edad: "))

print (( e >= 18 and "Mayor de edad") or "Menor de edad")

# literal b

s = int (input(" Ingrese su salario: "))

print ((s > 5000000 and "Su salario es alto") or "Su salario es bajo")

n1 = float ( input ("Ingrese la nota 1: ")) 
n2 = float ( input ("Ingrese la nota 2: "))
n3 = float ( input ("Ingrese la nota 3: "))

print ((n1 >= 3 and n2 >= 3 and n3 >=3 and "Pasa la materia") or " No pasa la materia")