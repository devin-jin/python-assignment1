import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()  # 创建画布和绘图区
# ax.set_axis_off()
x = np.arange(0, 2 * np.pi, 0.01)  # 生成X轴坐标序列
line1, = ax.plot(x, np.sin(x))  # 获取折线图对象，逗号不可少，如果没有逗号，得到的是元组
line2, = ax.plot(x, np.cos(x))  # 获取折线图对象，逗号不可少


def update(n):  # 动态更新函数
    line1.set_ydata(np.sin(x + n / 10.0))  # 改变线条y的坐标值
    line2.set_ydata(np.cos(x + n / 10.0))  # 改变线条y的坐标值


ani = FuncAnimation(fig, update, frames=1000, interval=50, blit=False, repeat=False)  # 创建动画效果
plt.show()  # 显示图 作者：手把手教你学编程 https://www.bilibili.com/read/cv13169116 出处：bilibili