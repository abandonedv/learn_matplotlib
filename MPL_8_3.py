import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import *

rect = Rectangle((1, 1), 2.5, 0.5, facecolor="g")

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.add_patch(rect)
ax.set(xlim=(0, 10), ylim=(0, 10))
plt.show()