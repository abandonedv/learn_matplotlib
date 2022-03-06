import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.arange(10)
y1 = np.random.randint(3, 20, len(x))
y2 = np.random.randint(3, 20, len(x))
w = 0.3
ax.bar(x - w/2, y1, width=w)
ax.bar(x + w/2, y2, width=w)

ax.grid()
plt.show()