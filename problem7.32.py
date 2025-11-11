import math
import matplotlib.pyplot as plt
from scipy import integrate

# (a)
def f(x, c, t):
    return math.sqrt(x) / (math.exp((x-c)/t) + 1)

# (b)
result_a, error_a = integrate.quad(f, 0, 100, args=(0, 1))
print(f'(a): {result_a: .3f}')

def get_c(t):
    upper = 1
    lower = -3
    mid = (upper + lower) / 2
    while True:
        result, error = integrate.quad(f, 0, 100 * t, args=(mid, t))
        if abs(result - 2/3) <= error:
            break
        elif result > 2/3:
            upper = mid
            mid = (mid + lower) / 2
        else:
            lower = mid
            mid = (mid + upper) / 2
    return mid

t = []
c = []
for i in range(100):
    t.append((i+1)/50)
    c.append(get_c((i+1)/50))

plt.scatter(t, c, s = 1)
plt.xlabel('t')
plt.ylabel('c')
plt.show()

# (c)
def u_func(x, c, t):
    return 2.5 * x**(1.5) / (math.exp((x-c)/t) + 1)
u = []
for i in range(100):
    result_u, error_u = integrate.quad(u_func, 0, 100 * t[i], args=(c[i], t[i]))
    u.append(result_u)

plt.scatter(t, u, s = 1)
plt.xlabel('t')
plt.ylabel('U / 0.6Ne_F')
plt.show()