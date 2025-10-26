import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return np.exp(-1/x) / (x**2)
x = np.linspace(0.01,10,500)
y = func(x)

plt.figure(num=3,figsize=(8,5))

plt.plot(x,y,color='red',linewidth=1.0)
plt.show()