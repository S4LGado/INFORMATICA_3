"""
Este modulo llamado logica,
mediante el cual se tienen
3 funciones logicas para:

- Sumar 3 numeros
- Sumar n numeros
- Sumar 2 listas elemento a elemento
"""

def suma3(a,b,c):
    sum = a + b + c
    return sum

def sumaN(*n):
    sum = 0
    # Otra forma es smnar la lista de numeros de la forma sum(n)
    for numero in n:
        resultado = sum + numero
    return resultado

def suma2Listas(a,b):
    resultado = []
    for i in range(0,len(a)):
        resultado.append(a[i]+b[i])
    return resultado
