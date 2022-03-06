import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import \
    NullFormatter, \
    FormatStrFormatter, \
    FuncFormatter, \
    ScalarFormatter, \
    FixedFormatter


def format0y(x, pos):
    return f"[{x}]" if x < 0 else f"({x})"


# это если мы хотим чтобы ограничение относилось ко всем графикам
matplotlib.rcParams["axes.formatter.limits"] = (-4, 4)

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi / 2, np.pi, 0.1)

ax.plot(x, np.sin(x) * 1e4)

# отключаем числовые значения на осях
# ax.set_xticklabels([])
# ax.set_yticklabels([])

# тоже отключаем числовые значения на осях
# ax.yaxis.set_major_formatter(NullFormatter())

# позволяет управлять отображением надписей у разметки
# ax.yaxis.set_major_formatter(FormatStrFormatter("y = %.3f"))

# позволяет вызывать функцию для формирования числовых значений
# ax.yaxis.set_major_formatter(FuncFormatter(format0y))

# sf = ScalarFormatter()
# sf.set_powerlimits((-4, 4))
# если степень > 4 то она вынесется за скобки, график адаптируется
# в противном случае все выведется как задано

# ax.yaxis.set_major_formatter(sf)

# каждой риске оси присваивает строго определенное значение
ax.yaxis.set_major_formatter(FixedFormatter(["e", "t", "d"]))

ax.grid()
plt.show()
