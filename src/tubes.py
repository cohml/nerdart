import matplotlib.pyplot as plt
import numpy as np

# params
n_tubes = 6

ax = plt.subplot()
ax.axis('off')

x = np.linspace(-np.pi, np.pi, 500)
for dot in range(2000):
    offset = np.random.random()
    for circle in range(1, n_tubes):
        ax.plot(np.cos(x) / circle + offset,
                np.sin(x) / circle - offset,
                color='k',
                alpha=0.01,
                ls=':')

plt.show()
