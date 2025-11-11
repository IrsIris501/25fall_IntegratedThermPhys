import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

# 定义拟合函数
def model_func(x, a, b):
    return 1 / (np.exp((x-a)/b) + 1)

# 示例数据（请替换为您的实际数据）
x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
y_data = np.array([11, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0])
y_data = y_data / 11


# 非线性曲线拟合
params, covariance = curve_fit(model_func, x_data, y_data)
a_fit, b_fit = params

# 计算R²
y_pred = model_func(x_data, a_fit, b_fit)
r_squared = r2_score(y_data, y_pred)

# 生成拟合曲线
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = model_func(x_fit, a_fit, b_fit)

# 绘制结果
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label='data', color='blue', s=50)
plt.plot(x_fit, y_fit, label=f'Curve: y = 1 / (np.exp((x - {a_fit:.3f}) / {b_fit:.3f}) + 1)', color='red', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Fitting 1 / (exp((x - a) / b) + 1)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 打印拟合结果
print(f"Result:")
print(f"a = {a_fit:.6f}")
print(f"b = {b_fit:.6f}")
print(f"R² = {r_squared:.6f}")