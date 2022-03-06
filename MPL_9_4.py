import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.random.normal(0, 2, 500)
y = np.random.normal(0, 2, 500)

# точечный график
ax.scatter(x, y, s=50, c="g", linewidths=1, marker="s", edgecolors="r")

ax.grid()

plt.show()