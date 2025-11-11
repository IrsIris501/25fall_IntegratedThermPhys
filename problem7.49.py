import math
import matplotlib.pyplot as plt
import scipy.integrate

#(d)
def get_u(x, t):
    return x**2 * math.sqrt(x**2 + t**(-2)) / (math.exp(math.sqrt(x**2 + t**(-2))) + 1)

t = []
u = []
for i in range(1, 101):
    t.append(i/10)
    result, error = scipy.integrate.quad(get_u, 0, 100, args=(i/10))
    u.append(result)

plt.scatter(t, u, s = 1)
plt.xlabel('kT/mc^2')
plt.ylabel('u(T)')
plt.show()

#(e)
def get_f(x, t):
    return x**2 * math.log(1 + math.exp(-math.sqrt(x**2 + t**(-2))))

t = []
f = []
for i in range(1, 101):
    t.append(i/10)
    result, error = scipy.integrate.quad(get_f, 0, 100, args=(i/10))
    f.append(result)

plt.scatter(t, f, s = 1)
plt.xlabel('kT/mc^2')
plt.ylabel('f(T)')
plt.show()

#(f)
def get_s(x):
    return x**3 / (1 + math.exp(x)) + x**2 * math.log(1 + math.exp(-x))

result, error = scipy.integrate.quad(get_s, 0, 100)
print(f's = {result: .3f}')