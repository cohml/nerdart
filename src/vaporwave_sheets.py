import matplotlib.pyplot as plt
import numpy as np

# tweakable parameters
n = 10
resolution = 1000
linestyles = ['-', ':', '--']

_, axes = plt.subplots(nrows=len(linestyles))

for i in np.linspace(0, n, resolution):

    for ax, ls in zip(axes, linestyles):
        ax.axis('off')

        x = np.linspace(0, 2 * np.pi, resolution)
        alpha = 0.15
        color = (i / n,
                 0,
                 1 - (i / n))

        ax.plot(x + (0.5 * i),
                np.sin(x),
                ls=ls,
                alpha=alpha,
                color=color)

plt.tight_layout()
plt.show()
