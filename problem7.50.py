import math
from scipy import integrate
import matplotlib.pyplot as plt

#(b)
def func(x):
    return x**3 / (math.exp(x)-1) - x**2 * math.log(1 - math.exp(-x))

result, error = integrate.quad(func, 0, 500)

result /= 2
print(result)

#(c)
def func2(x):
    return x**3 / (math.exp(x)+1) + x**2 * math.log(1 + math.exp(-x))
result2, error2 = integrate.quad(func2, 0, 500)
print((result / (result + result2))**(1/3))
print(f'T_v = {2.73 * (result / (result + result2))**(1/3): .3f}')

#(d)
def func3(x, t):
    return x**2 * math.sqrt(x**2 + t**(-2)) / (math.exp(math.sqrt(x**2 + t**(-2))) + 1) + x**2 * math.log(1 + math.exp(-math.sqrt(x**2 + t**(-2))))

t = [0]
ratio = [(result / (result + result2))**(-1/3)]
for i in range(1, 40):
    t.append(i / 100)
    temp, error = integrate.quad(func3, 0, 500, args=(i / 100))
    ratio.append(((result + temp) / (result + result2)) ** (-1 / 3))
for i in range(4, 31):
    t.append(i/10)
    temp, error = integrate.quad(func3, 0, 500, args=(i/10))
    ratio.append(((result + temp) / (result + result2))**(-1/3))

plt.scatter(t, ratio, s = 1)
plt.xlabel('kT/mc^2')
plt.ylabel('T/T_v')
plt.show()