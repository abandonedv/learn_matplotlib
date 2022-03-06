import numpy as np
import matplotlib.pyplot as plt

ax1 = plt.subplot(2, 3, 1)
print(np.random.random(10))
plt.plot(np.random.random(10))
ax2 = plt.subplot(2, 3, 2)
plt.plot(np.random.random(10))
ax3 = plt.subplot(2, 3, 3)
plt.plot(np.random.random(10))
ax4 = plt.subplot(2, 1, 2)
plt.plot(np.random.random(10))


ax1.grid()
ax2.grid()
ax3.grid()

plt.show()