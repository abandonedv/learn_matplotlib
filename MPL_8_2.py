import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

ax.set(xlim=(0, 10), ylim=(0, 10))
l1 = Line2D([1, 8, 4], [5, 3, 9])

ax.add_line(l1)

plt.show()
