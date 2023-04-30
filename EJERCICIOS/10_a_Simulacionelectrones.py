import numpy as np
import matplotlib.pyplot as plt

k=1
r = 1
T = 0.01
q = 1
elec_Circunferenciales = 20
elec_Internos = 10

def crear_Estado_Inicial():
    angulo = 6.28/(elec_Circunferenciales)
    x_out = [r*np.cos(ang) for ang in np.arange(0, 6.28, angulo)]
    y_out = [r*np.sin(ang) for ang in np.arange(0, 6.28, angulo)]
    x_in = [np.random.random() - 0.5 for i in range(elec_Internos)]
    y_in = [np.random.random() - 0.5 for i in range(elec_Internos)]
    return x_out,y_out,x_in,y_in

def dibujar_sistema(x_out,y_out,x_in,y_in):
    plt.figure()
    plt.plot(x_out,y_out, "ro")
    plt.plot(x_in, y_in, "bo")
    plt.gca().set_aspect("equal")
    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)
    plt.grid()
    plt.show()

x_out,y_out, x_in,y_in = crear_Estado_Inicial()
dibujar_sistema(x_out,y_out,x_in,y_in)

r=[]
for i in range(len(x_out)):
    r.append((x_out[i], y_out[i]))
for i in range(len(x_in)):
    r.append((x_in[i], y_in[i]))

print( "======", r)
def distancia(r1, r2):
    return ((r1[0]-r2[0])**2 + (r1[1]-r2[1])**2)**0.5

from itertools import combinations
def calcular_energia_total(r):
    sumEnergias = 0
    combinaciones = list(combinations(r, 2))
    for r_ in combinaciones:
        r1, r2 = r_[0], r_[1]
        sumEnergias += k*q*q / distancia(r1,r2)
    return sumEnergias

sumEnergias_old = calcular_energia_total(r)
print(sumEnergias_old)
def metropolis(x_in,y_in,sumEnergias_old):  #cambio aleatorio de la posicion de un electron interno
    x_old = x_in
    y_old = y_in
    x_new = [np.random.random() - 0.5 for i in range(elec_Internos)]
    y_new = [np.random.random() - 0.5  for i in range(elec_Internos)]
    r=[]
    for i in range(len(x_out)):
      r.append((x_out[i], y_out[i]))
    for i in range(len(x_new)):
      r.append((x_new[i], y_new[i]))
    sumEnergias_new = calcular_energia_total(r)
    if sumEnergias_new < sumEnergias_old:
      sumEnergias_old = sumEnergias_new
      print(sumEnergias_old)
      x_in = x_new
      y_in = y_new
    else:
      pass
    return x_new,y_new,x_in,y_in,sumEnergias_old

def paso_montecarlo(sumEnergias_old):
    x_new,y_new,x_in,y_in,sumEnergias_old = [],[],[],[],sumEnergias_old
    for i in range(0,1000000):
      x_new,y_new,x_in,y_in,sumEnergias_old = metropolis(x_in,y_in,sumEnergias_old)
    return x_new,y_new,x_in,y_in,sumEnergias_old

x_new,y_new,x_in,y_in,sumEnergias_old = paso_montecarlo(sumEnergias_old)

dibujar_sistema(x_out,y_out,x_in,y_in)
