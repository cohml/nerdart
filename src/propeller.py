import matplotlib.pyplot as plt
import numpy as np

n = 400

ax = plt.subplot(polar=True)
x = np.linspace(1.5*-np.pi, 1.5*np.pi, 10)

for i in np.linspace(0, n):
    ax.plot(x + i, np.tan(x)*np.sin(x) + i, ls=':', lw=7, alpha=1-i/n, color='k') # color=(1-i/n, 0, i/n)

ax.axis('off')
plt.show()
