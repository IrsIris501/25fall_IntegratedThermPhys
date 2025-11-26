import math
from matplotlib import pyplot as plt
import scipy.integrate

def func(x, c, t):
    return math.sqrt(x) / (math.exp((x-c)/t) - 1)

def get_cv(x, c, t):
    return 0.432 * x * (x-c) * math.sqrt(x) * math.exp((x-c)/t) / t**2 / (math.exp((x-c)/t) - 1) ** 2

def get_cv2(x, c, t):
    return 0.432 * x * math.sqrt(x) * math.exp((x-c)/t) / t / (math.exp((x-c)/t) - 1) ** 2

def get_u(x, c, t):
    return 0.432 * func(x, c, t) * x

def mid_test(mid, t):
    result, error = scipy.integrate.quad(func, 0, 500 * t, args = (mid, t))
    if abs(result - 2.315) < 0.001:
        return 0
    else:
        if result < 2.315:
            return -1
        else:
            return 1


cv = [0]
t = [0]
c_list = [0]
for i in range(300):
    temp = i * 0.01 + 0.01
    t.append(temp)
    if temp <= 1:
        c = 0
    else:
        left = -5
        right = 0
        mid = (left + right) / 2
        while True:
            test_result = mid_test(mid, temp)
            if not test_result:
                c = mid
                break
            elif test_result == -1:
                left = mid
                mid = (left + right) / 2
            else:
                right = mid
                mid = (left + right) / 2
    c_list.append(c)


for i in range(1, 300):
    temp = i * 0.01
    result, error = scipy.integrate.quad(get_cv, 0, 300 * temp, args = (c_list[i], temp))
    result2, error = scipy.integrate.quad(get_cv2, 0, 300 * temp, args = (c_list[i], temp))
    cv.append(result + result2 * (c_list[i+1] - c_list[i-1]) * 50)

plt.scatter(t[0:-1:1], cv, s = 1, color = 'red')
plt.title('Integral Method')
plt.xlabel('t')
plt.ylabel('Cv/Nk')
plt.show()


u = [0]
for i in range(1, 301):
    temp = i * 0.01
    result, error = scipy.integrate.quad(get_u, 0, 500 * temp, args = (c_list[i], temp))
    u.append(result)

cv_differ = [0]
for i in range(1, 300):
    cv_differ.append((u[i+1] - u[i-1]) * 50)

plt.scatter(t[0:-1:1], cv_differ, s = 1, color = 'blue')
plt.xlabel('t')
plt.ylabel('Cv/Nk')
plt.title('Differential Method')
plt.show()



