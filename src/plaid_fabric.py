import matplotlib.pyplot as plt
import numpy as np

mod = np.linspace(1, 0, 1000)
linspace = np.linspace(-np.pi*2, np.pi*2, 1000)

x = [linspace + 0.1*i for i in range(100)]
y = [np.sin(linspace) for _ in x]

ax = plt.subplot(projection=None)
ax.axis('off')

for i, (xi, yi) in enumerate(zip(x, y)):
    ax.plot(xi, yi*mod, alpha=1-i/len(x), color='k', lw=np.random.random()*5)

plt.show()
