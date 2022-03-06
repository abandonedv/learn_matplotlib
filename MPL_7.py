import numpy as np
import matplotlib.pyplot as plt

# y = np.arange(0, 5, 1)
# x = np.array([a**2 for a in y])

fig = plt.figure(figsize=(7, 4))
fig.set(facecolor="#eee")
ax = fig.add_subplot()
ax.set(facecolor="#AAFFAA")
plt.figtext(0.05, 0.6, "Текст в области окна", fontsize=24, color="red")
fig.suptitle("Заголовок окна")
ax.set_xlabel("Ox")
ax.set_ylabel("Ox")
# plt.xlabel("Ox") Применяются к активной координатной оси
# plt.ylabel("Ox")
ax.text(0.05, 0.1, "Произвольный текст в координатных осях",
        bbox={"boxstyle": "darrow", "facecolor": "#AAAAFF"})
ax.annotate("Аннотация", xy=(0.1, 0.9), xytext=(0.6, 0.9),
            arrowprops={"facecolor": "gray", "shrink": 0.1})

# y2 = [0, 2, 3, 4, 5, 7]
# x2 = [i+1 for i in y2]
# lines = plt.plot(x, y, x2, y2)
#
# plt.minorticks_on()
# plt.grid(which="major", color="#444", linewidth=1)
# plt.grid(which="minor", color="#aaa", ls=":")
# plt.grid()
plt.show()
