import matplotlib.pyplot as plt
import numpy as np

# params
n_shapes = 25
n_angles = 3

coords = np.linspace(-np.pi, np.pi, n_angles + 1)
nrows = ncols = int(np.ceil(np.sqrt(n_shapes)))
ax = plt.subplot(polar=False)

for row in range(3, nrows + 3):
	for col in range(3, ncols + 3):
		I = np.linspace(0, 2 * np.pi, row)
		C = plt.cm.autumn(np.linspace(0, 1, I.size))

		for i, c in zip(I, C):
			x = np.sin(coords + i + row) + i + row * 4 + np.random.random()
			y = np.cos(coords + i + col) + i + col * 4 + np.random.random()
			a = np.clip(1 - i / I.max(), 0.2, 1)
			c[-1] = a

			ax.plot(x, y, lw=1, c=c, zorder=col)
			ax.fill(x, y, color=c)

ax.axis('off')
plt.show()
