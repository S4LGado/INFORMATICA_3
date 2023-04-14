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

# Visualizacin de los espines

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

plot_spins()