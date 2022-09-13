""" Realice los siguientes programas:
      a) Programa que calcule los primeros 100 terminos de la serie de fibonacci
      b) Programa que determine todos los divisores de un numero n
      c) Programa que determine si un número n es primo
      d) Programa que sume los digitos de un numero cualquiera. Ejemplo: numero=> 8791, rta=> 25 
      e) Programa que sume los digitos pares de un numero cualquiera """

# Literal a

fibonacci1 = 1
fibonacci2 = 1
for i in range (1,100):

    fibonacci3 = fibonacci1 + fibonacci2
    print (fibonacci3)
    fibonacci1= fibonacci2
    fibonacci2= fibonacci3

# literal b

n = int (input("Digite un número: "))
divisores = 1
for i in range (1,n):
    e = n % i
    if e == 0:
        divisores = divisores + 1

print("Tiene ",divisores," divisores")

#  literal c

divisores = 1
primo = 1
for i in range (2,(n-1)):
    e = n % i
    if e == 0:
        primo = 0

if primo == 0:
    print("Este número no es primo")
elif primo == 1:
    print("Este número es primo")

# literal d

sumadigitos = 0
sumadigitos2 = 0
unum = 0
m = n 
while   m != 0:
    unum = m % 10
    m = m // 10
    sumadigitos = sumadigitos + unum
    if unum % 2 == 0:
        sumadigitos2 = sumadigitos2 + unum
print ("La suma de los digitos es: ", sumadigitos)

# literal e
print ("La suma de los digitos pares es: ", sumadigitos2)