import matplotlib.pyplot as plt
import numpy as np

# params
n_pipes = 25
width = 10

coords = np.linspace(-np.pi, np.pi, 5 * n_pipes)
pipe = [np.sin(coords) * width,
        np.cos(coords) * width]

for i in range(n_pipes):
	orient = np.random.choice([-1, 1])
	length = np.random.randint(1, 10)
	direction = i % 2

	for j in range(length * width * 2):
		pipe[direction] += orient
		plt.plot(*pipe, c='k', alpha=1/n_pipes, zorder=i)

plt.gca().set_aspect('equal')
plt.tight_layout()
plt.axis('off')
plt.show()
