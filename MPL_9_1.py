import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

x = np.arange(0, 10, 0.5)
ax.step(x, np.cos(x), "-o", where="pre")
plt.show()
