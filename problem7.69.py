import math
from matplotlib import pyplot as plt
import scipy.integrate

def func(x, c, t):
    return math.sqrt(x) / (math.exp((x-c)/t) - 1)

# (b)
result, error = scipy.integrate.quad(func, 0, 1000, args = (-0.8, 2))
print(f'result = {result: .3f}')

# (c)
c = []
t = []

def mid_test(mid, t):
    result, error = scipy.integrate.quad(func, 0, 500 * t, args = (mid, t))
    if abs(result - 2.315) < 0.001:
        return 0
    else:
        if result < 2.315:
            return -1
        else:
            return 1

for i in range(10):
    temp = i * 0.2 + 1.2
    t.append(temp)
    left = -5
    right = 0
    mid = (left + right) / 2
    while True:
        test_result = mid_test(mid, temp)
        if not test_result:
            c.append(mid)
            break
        elif test_result == -1:
            left = mid
            mid = (left + right) / 2
        else:
            right = mid
            mid = (left + right) / 2

plt.scatter(t, c)
plt.xlabel('t')
plt.ylabel('c')
plt.show()



