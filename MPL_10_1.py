import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

y = np.random.normal(0, 2, 500)
print(y)
ax.hist(y, 50)
ax.grid()

plt.show()