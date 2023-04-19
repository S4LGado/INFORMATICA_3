import numpy as np
import matplotlib.pyplot as plt

k = 1
r = 1
temp = 0.01

elec_Circunferenciales = 15
elec_Internos = 1000

angulo = 6.28/elec_Circunferenciales
x_out = [r*np.cos(ang) for ang in np.arange(0, 6.28, angulo)]
y_out = [r*np.sin(ang) for ang in np.arange(0, 6.28, angulo)]

x_in1 = [0.9*r*np.cos(ang-3) for ang in np.arange(0, 6.28, angulo)]
y_in1 = [0.9*r*np.sin(ang-3) for ang in np.arange(0, 6.28, angulo)]

x_in = [0.95*r*np.cos(ang-2) for ang in np.arange(0, 6.28, angulo)]
y_in = [0.95*r*np.sin(ang-2) for ang in np.arange(0, 6.28, angulo)]


plt.figure()
plt.plot(x_out,y_out,"ro")
plt.plot(x_in, y_in, "bo")
plt.plot(x_in1, y_in1, "yo")
plt.plot()
plt.gca().set_aspect("equal")
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)
plt.show