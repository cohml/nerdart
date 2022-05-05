import matplotlib.pyplot as plt
import numpy as np

# params
n = 15

ax = plt.subplot()
ax.axis('off')

x = np.logspace(0, 1000, 5000)

for i in range(n):
    ax.plot(np.cos(x) + i, np.sin(x) * i, color='k', alpha=i/n, lw=10)

plt.show()
