import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import \
    NullLocator, \
    LinearLocator, \
    MultipleLocator, \
    IndexLocator, \
    FixedLocator, \
    LogLocator, \
    MaxNLocator


fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
# ax.plot(np.arange(1, 5, 0.25))

# для IndexLocator
x = np.arange(-np.pi/2, np.pi, 0.1)
ax.plot(x, np.sin(x))

ax.minorticks_on()
ax.grid(which="major", lw=2)
ax.grid(which="minor")

ax.xaxis.set_minor_locator(NullLocator())

# отключает метки (линии) по выбранной оси
# ax.xaxis.set_major_locator(NullLocator())

# задает нужное число меток по выбранной оси
# ax.xaxis.set_major_locator(LinearLocator(6))

# задает шаг изменения значения между разметкой (рисками)
# ax.xaxis.set_major_locator(MultipleLocator(base=3))

# делает то же самое но производит отсчет не от нуля,
# а от наименьшего значения графика
# ax.xaxis.set_major_locator(IndexLocator(base=0.5, offset=0.57))

# устанавливает метки в указанных значениях
# ax.xaxis.set_major_locator(FixedLocator([-2, -1, 0, 1, 2, 3]))

# формирование логарифмических делений по осям
# ax.xaxis.set_major_locator(LogLocator(base=2))

# разбивка по нужной координате на указанное число рисок
# но разбивка выполняется в наиболее удобном виде
# то есть разбивка может быть меньше если при больших значения некрасиво
# ax.xaxis.set_major_locator(MaxNLocator(5))

plt.show()