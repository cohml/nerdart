import matplotlib.pyplot as plt
import numpy as np

# params
n = 10
width = 1

coords = np.linspace(-np.pi, np.pi, 50)
X = np.sin(coords) * width
Y = np.cos(coords) * width

I = np.linspace(-np.pi * n / 2, np.pi * n / 2, 1000 * n)
C = plt.cm.gist_rainbow(np.linspace(1, 0, 1000 * n))

for i, c in zip(I, C):
	x = X + np.sin(i * 2) + i
	y = Y + np.sin(i) * i

	plt.plot(x, y, c=c, alpha=0.5 / n)

plt.axis('off')
plt.show()
