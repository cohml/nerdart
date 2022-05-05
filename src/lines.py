import matplotlib.pyplot as plt
import numpy as np
from random import random, shuffle

n_lines = 50
max_lw = 5

x = list(range(n_lines))
y = list(range(n_lines))

shuffle(y)

for i in range(n_lines-1):
    plt.plot([x[i], x[i]],
             [y[i], y[i+1]],
             alpha=random(),
             lw=max_lw*i/n_lines+1)

plt.axis('off')
plt.show()
