import matplotlib.pyplot as plt
import numpy as np

# params
length = 3

ax = plt.subplot(projection='3d')

x = np.linspace(-np.pi * length, np.pi * length, 1000 * length)
y = np.sin(x)
z = np.cos(x)

ax.bar(x, y, z, color=plt.cm.gist_rainbow(np.linspace(0, 1, x.size)))
ax.axis('off')

plt.show()

