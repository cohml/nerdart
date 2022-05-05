import matplotlib.pyplot as plt
import numpy as np

# params
n = 10

coords = np.linspace(-np.pi, np.pi, 8)
X = np.sin(coords)
Y = np.cos(coords)

I = np.linspace(0, np.pi * n, 5000)
C = plt.cm.rainbow(np.linspace(1, 0, 5000))

for i, c in zip(I, C):
	x = X * np.sin(i) * i + i * 2
	y = Y * np.cos(i) * i + i * 2
	plt.plot(x, y, c=c, alpha=0.02)

plt.axis('off')
plt.tight_layout()
plt.show()
