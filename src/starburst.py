import matplotlib.pyplot as plt
import numpy as np

# params
dot = False
n = 15

ax = plt.subplot(polar=False)
ax.axis('off')
x = np.linspace(1, 1000, 100)

if dot:
    plot = ax.scatter
else:
    plot = ax.plot

for i in range(n):
    plot(np.sin(x) * i, np.cos(x) * i, alpha=i/n, color='k', lw=0.5)

plt.show()
