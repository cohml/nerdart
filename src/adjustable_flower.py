
import matplotlib.pyplot as plt
import numpy as np

# params
bleep = -100
bloop = 100
blap = 1000

coords = np.linspace(np.pi * bleep, np.pi * bloop, blap)
x = np.sin(coords)
y = np.cos(coords)
colors = plt.cm.prism(np.linspace(0, 1, blap))

ax = plt.subplot()
ax.scatter(x * (x + coords), y * (y + coords), c=colors, alpha=0.75)
ax.set_aspect('equal')
ax.axis('off')

plt.show()

