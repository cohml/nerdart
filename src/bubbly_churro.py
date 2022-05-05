import matplotlib.pyplot as plt
import numpy as np

# params
n_twists = 3

x = np.linspace(-np.pi * n_twists, np.pi * n_twists, 100)
c = plt.cm.gist_rainbow(np.linspace(0, 1, x.size))

for i in np.linspace(0, 10, 100):
	y = np.sin(x + i) + i
	plt.scatter(x, y, alpha=0.2, c=c)

plt.tight_layout()
plt.axis('off')
plt.show()
