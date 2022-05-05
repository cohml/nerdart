import matplotlib.pyplot as plt
import numpy as np

# params
ndots = 50
density = 25   # mutually
orbitals = 10  # dependent
ngons = 4
zoom = 5

nums = np.linspace(-np.pi, np.pi, ngons + 1)
dotx = np.sin(nums)
doty = np.cos(nums)

ax = plt.subplot()

jitters = []
for dot in range(ndots):

	jitterx = np.random.random() * zoom
	jittery = np.random.random() * zoom

	for i in np.linspace(1, orbitals, density):
		ax.plot(dotx/i + jitterx, doty/i + jittery, c='k', lw=0.25, alpha=np.random.random())

ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.show()
