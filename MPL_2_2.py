from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x)
plt.plot(x, y)
plt.fill_between(x, y, where=(y < 0), color="r", alpha=0.5)
plt.fill_between(x, y, where=(y > 0), color="g", alpha=0.5)

plt.grid()
plt.show()