from matplotlib import pyplot as plt
import numpy as np

# x = np.arange(4, 9)
# y = np.array([1, 2, -6, 0, 4])
# plt.plot(x, y)

x1 = np.array([1, 1, 5, 5, 1])
y1 = np.array([1, 5, 5, 1, 1])
plt.plot(x1, y1, "--r", marker="*")

x3 = np.arange(6)
y3 = np.array([y**2 for y in x3])
plt.plot(x3, y3, marker="s", markerfacecolor="g")

x2 = [0, 1, 2, 3]
y2 = [i + 1 for i in x2]
line = plt.plot(x2, y2)
plt.setp(line, linestyle=':', color="b", linewidth=4)

plt.grid()
plt.show()
