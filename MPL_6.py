import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.arange(-10 * np.pi, 10 * np.pi, 0.5)

# логарифминеский маштаб у координатных осей
# ax.semilogy(x, np.sinc(x) * np.exp(-np.abs(x/10)))

ax.plot(x, np.sinc(x) * np.exp(-np.abs(x/10)))
ax.set_yscale("log")
ax.set_xscale("log")
 
ax.grid()
plt.show()
