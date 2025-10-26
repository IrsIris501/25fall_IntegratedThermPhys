import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 定义函数
def T(x, t):
    return 1 / np.sqrt(t) * np.exp(- x**2 / (4*t))


# 设置参数
x_values = np.linspace(0, 2*np.pi, 100)
t_values = np.linspace(0.1, 10, 99)

# 创建图形
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot(x_values, T(x_values, 0.1), 'r-', linewidth=2)

# 设置图形属性
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.1, 1.1)
ax.set_xlabel('x')
ax.set_ylabel('T(x,t)')
ax.set_title('T(x,t) vs x')
ax.grid(True)

# 动画更新函数
def update(frame):
    t = t_values[frame]
    line.set_ydata(T(x_values, t))
    ax.set_title(f'T(x,t) vs x animation')
    return line,

# 创建动画
ani = FuncAnimation(fig, update, frames=len(t_values), interval=200, blit=True)
plt.show()

# 如果要保存动画，可以取消下面一行的注释
# ani.save('T_evolution.mp4', writer='ffmpeg', fps=10)
