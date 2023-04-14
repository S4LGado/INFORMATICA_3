import numpy
from collections import defaultdict
from matplotlib import pyplot
import itertools

# Longitud del sistema
length = 10
# Constante de intercambio
J = 1.0
# Constante de boltzmann
kB = 1.0

# Contenedores
sites = list() # Contenedor de posiciones
spins = dict() # Contenedor de spins
nbhs = defaultdict(list) # Contenedor de vecinos

# Creacion de la muestra

for x, y in itertools.product(range(length), range(length)):
    sites.append((x,y))

# Creación del Estado incial aleatorio

def random_configuration():
    for spin in sites:
        spins[spin] = numpy.random.choice([-1, 1])

random_configuration()

# Visualizacion de los espines

def plot_spins():
    pyplot.figure()
    colors = {1: "orange", -1: "green"} # Color de las flechas
    for site, spin in spins.items():
        x, y = site
        pyplot.quiver(x, y, 0, spin, pivot="middle", color=colors[spin])
    pyplot.xticks(range(-1,length+1)) # Rango en eje X
    pyplot.yticks(range(-1,length+1)) # Rango en eje Y
    pyplot.gca().set_aspect("equal") # Esto se agrega para que la grafica no sea mas ancha de lo normal
    #pyplot.grid()
    pyplot.savefig()
    pyplot.show()

# Asignacion de vecinos

nbhs = defaultdict(list) # Diccionario de vecinos
for site in spins.keys:
    x, y = site
    if x + 1 < length: # Vecino por la derecha
        nbhs[site].append(((x + 1) % length, y))
    if x - 1 >= 0:     # Vecino por la izquierda
        nbhs[site].append(((x - 1) % length, y))
    if y + 1 < length: # Vecino por encima
        nbhs[site].append((x, (y + 1) % length))
    if y - 1 >= 0:     # Vecino por debajo
        nbhs[site].append((x, (y - 1) % length))

# Definiciones para calculo de energia

def energy_site(site):
    energy = 0.0 
    for nbh in nbhs[site]:
        energy += spins[site] * spins[nbh] #Hamiltoniano
    return -J * energy

def total_energy():
    energy = 0.0
    for site in sites:
        energy += energy_site(site) #Suma de los Hamiltonianos
    return 0.5 * energy

def magnetization():
    mag = 0.0
    for spin in spins.values():
        mag += spin #Suma de los spines, si es aleatorio tiende a 0
    return mag

# Implementacion del algoritmo Metropolis 

def metropolis(site, T):
    oldSpin = spins[site]
    oldEnergy = energy_site(site)
    spins[site] *= -1
    newEnergy = energy_site(site)
    deltaE = newEnergy - oldEnergy
    if deltaE <= 0:
        pass
    else:
        if numpy.random.uniform(0, 1) <= numpy.exp(-deltaE/(kB*T)): #Aqui radica el modelo de montecarlo
            pass
        else:
            spins[site] *= -1

# Definicion del paso de montecarlo

def monte_carlo_step(T):
    for i in range(len(sites)):
        int_rand_site = numpy.random.randint(0, len(sites))
        rand_site = sites[int_rand_site]
        metropolis(rand_site, T)

# Simulacion

amount_mcs = 10000 # Pasos montecarlo
T_high = 5.0 
T_low = 0.01
step = -0.1

# Ciclo de Temperatura

temps = numpy.arange(T_high, T_low, step)
energies = numpy.zeros(shape=(len(temps), amount_mcs))
magnetizations = numpy.zeros(shape=(len(temps), amount_mcs))
random_configuration()
for ind_T, T in enumerate(temps):
    for i in range(amount_mcs):
        monte_carlo_step(T)
        energies[ind_T, i] = total_energy()
        magnetizations[ind_T, i] = magnetization()