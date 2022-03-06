import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

vals = [10, 40, 23, 30, 7]
labels = ["Tayota", "BMV", "Lexus", "Audi", "Lada"]
exp = (0.1, 0.2, 0, 0, 0)
ax.pie(vals, labels=labels, autopct="%.2f", explode=exp, shadow=True)

ax.grid()

plt.show()