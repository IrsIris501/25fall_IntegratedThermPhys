import matplotlib.pyplot as plt
import numpy as np


def n_bar(x, beta):
    return (np.exp(beta * (x - 1)) + 2) / (np.exp(2 * beta * (x - 1)) + np.exp(beta * (x - 1)) + 1)


x = np.linspace(-10, 10, 500)
n_high = n_bar(x, 0.1)
n_med = n_bar(x, 1)
n_low = n_bar(x, 10)


plt.plot(x, n_high, color = 'red', linewidth = 1.0, label = 'high temp, kT = 10 u0')
plt.plot(x, n_med, color = 'blue', linewidth = 1.0, label = 'med temp, kT = 1 u0')
plt.plot(x, n_low, color = 'green', linewidth = 1.0, label = 'low temp, kT = 0.1 u0')
plt.xlabel('e/u0')
plt.ylabel('n_bar')
plt.legend()
plt.show()