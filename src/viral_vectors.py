import matplotlib.pyplot as plt
import numpy as np
import random

n_lines = 1000
n_cols = 50
x_ticks = np.arange(n_cols)
for row in x_ticks:
    plt.scatter(x_ticks, [row]*n_cols, c='k', s=0.5)

x = [random.choice(x_ticks) for i in range(n_lines)]
y = [random.randint(0, len(x_ticks)-1) for i in range(n_lines)]

#plt.plot(x, y, lw=0.2)
for i in range(len(x) - 1):
    plt.plot((x[i], x[i+1]), (y[i], y[i+1]), lw=random.random())

plt.show()