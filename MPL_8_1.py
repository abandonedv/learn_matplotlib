import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

# ax.plot(np.arange(0, 5, 0.25), "--o", label="line 1")
# ax.plot(np.arange(0, 10, 0.5), ":s", label="line 2")
# ax.legend()

# 2й вариант
# ax.legend(["1", "2"])

line1, = ax.plot(np.arange(0, 5, 0.25), "--o", label="line 1")
line2, = ax.plot(np.arange(0, 10, 0.5), ":s", label="line 2")

# укзание положения легенды с помощью аргумента loc
# ax.legend((line2, line1), ["number2", "number1"], loc="upper right")

# укзание положения легенды с помощью аргумента bbox_to_anchor
ax.legend((line2, line1), ["number2", "number1"], bbox_to_anchor=(1, 0.7), facecolor="#aaa", framealpha=0.5)
plt.show()