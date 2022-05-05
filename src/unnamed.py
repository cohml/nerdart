import matplotlib.pyplot as plt
import numpy as np

# params
blurriness = 1 #4
n_rings = 30

ax = plt.subplot()
ax.axis('off')

linspace = np.linspace(-np.pi, np.pi, 1000)
x = np.sin(linspace)
y = np.cos(linspace)

for blur in range(blurriness):
    ring_x = x + np.random.random()
    ring_x_median = np.median(ring_x)

    ring_y = y + np.random.random()
    ring_y_median = np.median(ring_y)

    for ring in range(1, n_rings + 1):
        ax.plot([xi + ring if xi > ring_x_median else xi - ring for xi in ring_x],
                [yi + ring if yi > ring_y_median else yi - ring for yi in ring_y],
                color='k',
                lw=(10 / blurriness) * ring / n_rings)

plt.show()
