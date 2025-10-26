import matplotlib.pyplot as plt
import numpy as np

enthalpy_a = 670.3
enthalpy_b = 820.7
ta = 77.36
tb = 90.15

def x_g(x):
    return (1 - np.exp(enthalpy_a * (1/x - 1/ta)))/(np.exp(enthalpy_b * (1/x - 1/tb)) - np.exp(enthalpy_a * (1/x - 1/ta)))

def x_l(x):
    return x_g(x) * np.exp(enthalpy_b * (1/x - 1/tb))

x = np.linspace(75, 91, 500)
y = x_g(x)
z = x_l(x)

plt.figure(num = 3,figsize = (8,5))

plt.plot(y, x, color = 'red', linewidth = 1.0, label = 'x_g')
plt.plot(z, x, color = 'blue', linewidth = 1.0, label = 'x_l')
plt.xlabel('x')
plt.ylabel('T/K')
plt.legend()
plt.show()