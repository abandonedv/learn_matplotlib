import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = [f"H{i+1}" for i in range(10)]
y = np.random.randint(-20, 20, len(x))

ax.bar(x, y, width=0.5, linewidth=2, edgecolor="r", yerr=2, bottom=10)
ax.grid()

plt.show()