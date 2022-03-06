import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.arange(-np.pi, np.pi, 0.3)

# bottom базоый уровень
ax.stem(x, np.cos(x), "--r", "^g", ":", bottom=0.5)

ax.grid()

plt.show()