import matplotlib.pyplot as plt
import numpy as np

n = 1000

for j in (1, -1):
    for i in range(0, n, 200):
        for si in range(-i, i):
            x = np.linspace(-np.pi * 1.5, np.pi * 1.5, abs(si))
            y =  si + i + (np.sin(x) * si)
            x *= j

            alpha = abs(si / n)
            color = (abs(si/n),
                     0,
                     1 - abs(si / n))

            plt.plot(x,
                     y,
                     zorder=-i,
                     color=color,
                     alpha=alpha,
                     lw=0.1)

plt.axis('off')
plt.tight_layout()
plt.show()
