
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.special import eval_legendre
from matplotlib.animation import FuncAnimation




# №1
x = np.linspace(-1, 1, 100)

plt.figure(figsize=(10, 6))
plt.title('Полиномы Лежандра')
for n in range(1, 8):
    y = eval_legendre(n, x)
    plt.plot(x, y, label=f'n = {n}')

plt.legend(loc='upper right')

plt.grid(True)
plt.show()


# # №2
# t = np.linspace(0, 2*np.pi, 1000)
# frequencies = [(3, 2), (3, 4), (5, 4), (5, 6)]
#
# plt.figure(figsize=(12, 8))
# for idx, (a, b) in enumerate(frequencies, 1):
#     x = np.sin(a*t)
#     y = np.sin(b*t)
#     plt.subplot(2, 2, idx)
#     plt.plot(x, y)
#     plt.title(f'Соотношение частот: {a}:{b}')
#     plt.axis('equal')
#
# plt.tight_layout()
# plt.show()


# # №3
#
# fig, ax = plt.subplots()
# ax.set_aspect('equal')
# ax.set_xlim(-1.5, 1.5)
# ax.set_ylim(-1.5, 1.5)
# line, = ax.plot([], [], lw=2)
#
# def init():
#     line.set_data([], [])
#     return line,
#
# def update(frame):
#     t = np.linspace(0, 4 * np.pi, 1000)
#     a = 3 * frame
#     b = 2 - frame
#
#     x = np.sin(a * t)
#     y = np.sin(b * t)
#
#     x = x - x.mean()
#     y = y - y.mean()
#
#     line.set_data(x, y)
#     return line,
#
# a = FuncAnimation(fig, update, frames=np.linspace(0, 1, 200), init_func=init, blit=True, interval=50)
#
# plt.title('Анимация вращения фигуры Лисажу')
# plt.show()


# #№4
#
# fig, (ax_wave1, ax_wave2, ax_sum) = plt.subplots(1, 3, figsize=(15, 5))
#
#
# def create_wave(freq, amp):
#     x = np.linspace(0, 1, 1000)
#     y = amp * np.sin(2 * np.pi * freq * x)
#     return x, y
#
#
# freq1 = 1.0
# amp1 = 0.5
# freq2 = 2.0
# amp2 = 0.3
#
#
# def update_plot(val):
#     freq1 = s_freq1.val
#     amp1 = s_amp1.val
#     freq2 = s_freq2.val
#     amp2 = s_amp2.val
#
#     x, y1 = create_wave(freq1, amp1)
#     x, y2 = create_wave(freq2, amp2)
#
#     y_sum = y1 + y2
#
#     ax_wave1.clear()
#     ax_wave1.plot(x, y1)
#     ax_wave1.set_title('Wave 1')
#
#     ax_wave2.clear()
#     ax_wave2.plot(x, y2)
#     ax_wave2.set_title('Wave 2')
#
#     ax_sum.clear()
#     ax_sum.plot(x, y_sum)
#     ax_sum.set_title('Sum of Waves')
#
#     fig.canvas.draw_idle()
#
#
# ax_freq1 = plt.axes([0.1, 0.05, 0.3, 0.03])
# s_freq1 = Slider(ax_freq1, 'Freq 1', 1.0, 10.0, valinit=freq1)
# s_freq1.on_changed(update_plot)
#
# ax_amp1 = plt.axes([0.1, 0.01, 0.3, 0.03])
# s_amp1 = Slider(ax_amp1, 'Amp 1', 0.1, 1.0, valinit=amp1)
# s_amp1.on_changed(update_plot)
#
# ax_freq2 = plt.axes([0.55, 0.05, 0.3, 0.03])
# s_freq2 = Slider(ax_freq2, 'Freq 2', 1.0, 10.0, valinit=freq2)
# s_freq2.on_changed(update_plot)
#
# ax_amp2 = plt.axes([0.55, 0.01, 0.3, 0.03])
# s_amp2 = Slider(ax_amp2, 'Amp 2', 0.1, 1.0, valinit=amp2)
# s_amp2.on_changed(update_plot)
#
# update_plot(None)
#
# plt.show()



# #№5
#
# X = np.linspace(-5, 5, 100)
# Y = np.linspace(-5, 5, 100)
# X, Y = np.meshgrid(X, Y)
# Z = np.sqrt(X**2 + Y**2)
#
# Z_log = np.log(Z)
#
# fig = plt.figure(figsize=(12, 6))
#
# ax1 = fig.add_subplot(121, projection='3d')
# ax1.plot_surface(X, Y, Z, cmap='viridis')
# ax1.set_title('Среднеквадратичное отклонение MSE')
# ax1.set_xlabel('X')
# ax1.set_ylabel('Y')
# ax1.set_zlabel('Z')
#
# ax2 = fig.add_subplot(122, projection='3d')
# ax2.plot_surface(X, Y, Z_log, cmap='plasma')
# ax2.set_title('В логарифмическом масштабе')
# ax2.set_xlabel('X')
# ax2.set_ylabel('Y')
# ax2.set_zlabel('log(Z)')
#
# plt.show()