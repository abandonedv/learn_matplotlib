import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.25))

# ax.set_xlim(-5, 30)
# ax.set_ylim(-1, 6)

plt.xlim(-1, 20)
plt.ylim(-1, 6)

plt.show()