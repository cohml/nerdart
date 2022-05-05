import matplotlib.pyplot as plt
import numpy as np

## params
roundness = None or 5
width = None or 1.5
shrinkray = None or 3
threshold = None or 1  # should prob keep b/w 0 and 1
nrows = ncols = None or 100

coords = np.linspace(-np.pi, np.pi, roundness) + np.pi / 4
x = np.sin(coords) / shrinkray
y = np.cos(coords) / shrinkray

ax = plt.subplot(aspect='equal')
ax.axis('off')

for row in range(nrows):
    for col in range(ncols):
        odds = col / ncols + np.random.random() ** 2
        ax.plot(col + x + odds * (odds > threshold),
                row + y + odds * (odds > threshold),
                lw=width * (ncols - col) / ncols,
                c='k')

plt.tight_layout()
plt.show()
