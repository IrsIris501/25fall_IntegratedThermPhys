import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

# 定义拟合函数
def model_func(x, a, b):
    return b - a / x

# 示例数据（请替换为您的实际数据）
x_data = np.array([100, 200, 300, 400, 500, 600])
y_data = np.array([-160, -35, -4.2, 9, 16.9, 21.3])

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
plt.plot(x_fit, y_fit, label=f'Curve: y = {b_fit:.3f} - {a_fit:.3f}/x', color='red', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Fitting y = b - a/x')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 打印拟合结果
print(f"Result:")
print(f"a = {a_fit:.6f}")
print(f"b = {b_fit:.6f}")
print(f"R² = {r_squared:.6f}")