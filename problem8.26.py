import random
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

size = 500
T = 2.28

def next_ij(x):
    return x + 1 if x != size - 1 else 0


def last_ij(x):
    return x - 1 if x else size - 1


def delta_u(s: list[list[int]], i, j):
    return 2 * s[i][j] * (s[next_ij(i)][j] + s[i][next_ij(j)] + s[last_ij(i)][j] + s[i][last_ij(j)])


num_frames = 100 * size * size
# num_frames = 100000

'''
# 这里的部分用来生成动画
lattice = [[[random.choice([0, 1]) for j in range(size)] for i in range(size)] for _ in range(num_frames)]

fig, ax = plt.subplots(figsize=(10, 10))

im = ax.imshow(lattice[0], cmap='gray')
plt.xticks([])
plt.yticks([])
ax.set_title("Frame 0")

def update(frame):

    lattice[frame] = lattice[frame - 1]
    i = int(random.random() * size)
    j = int(random.random() * size)
    if delta_u(lattice[frame], i, j) <= 0:
        lattice[frame][i][j] = -lattice[frame][i][j]
    else:
        if random.random() < math.exp(-delta_u(lattice[frame], i, j) / T):
            lattice[frame][i][j] = -lattice[frame][i][j]
    im.set_array(lattice[frame])
    ax.set_title(f"T = {T} Frame {frame}")
    return [im]


anim = FuncAnimation(fig, update, frames=num_frames, interval=10)
anim.save(f'animation T = {T}.mp4', writer='ffmpeg')
print('successfully saved')

'''

# 这里的部分用来生成图片
lattice = [[random.choice([-1, 1]) for j in range(size)] for i in range(size)]

for _ in range(num_frames):
    i = int(random.random() * size)
    j = int(random.random() * size)
    if delta_u(lattice, i, j) <= 0:
        lattice[i][j] = -lattice[i][j]
    else:
        if random.random() < math.exp(-delta_u(lattice, i, j) / T):
            lattice[i][j] = -lattice[i][j]

temp = 0
for i in range(size):
    temp += sum(lattice[i])
mag = abs(temp / size / size)
plt.imshow(lattice, cmap='gray')
plt.title(f'T = {T}, avg magnetization = {mag: .2f}')
plt.xticks([])
plt.yticks([])
plt.show()
# '''