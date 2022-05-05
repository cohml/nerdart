import matplotlib.pyplot as plt
import numpy as np

# params
polar = True
n = 15

ax = plt.subplot(polar=polar)
ax.axis('off')

x = np.logspace(0, 1000, 100)

for i in range(n):
    ax.plot(np.cos(x) * i, np.sin(x)*x * i, color='k', alpha=i/n)

plt.show()
