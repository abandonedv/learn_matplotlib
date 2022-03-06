import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

y = np.random.normal(0, 2, 500)
x = np.linspace(np.min(y), np.max(y), 10)
bars = [len(y[np.bitwise_and(y >= x[i],
                             y < x[i + 1])])
        for i in range(len(x) - 1)]

# ax.bar(range(len(x) - 1), bars)

# по горизонтали
ax.barh(range(len(x) - 1), bars)

ax.grid()
plt.show()
