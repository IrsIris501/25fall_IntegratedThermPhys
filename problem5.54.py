import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return -0.8 * np.log(x - 1/3) - (9/8) * (1/x)
x = np.linspace(0.4,1.5,500)
y = func(x)

plt.figure(num=3,figsize=(8,5))

plt.plot(x,y,color='red',linewidth=1.0)
plt.show()