import matplotlib.pyplot as plt
import numpy as np

# params
swirls = 1
sparsity = 1
thickness = 10

coords = np.linspace(0, 1, 10)
lines = np.linspace(-10 * sparsity, 10 * swirls, 100 * swirls)
lines_normed = (lines - lines.min())/np.ptp(lines) # squash b/w 0 and 1 for cm
colors = plt.cm.gist_rainbow(lines_normed)
lw = max(0, np.log10(thickness)) + 1e-10

ax = plt.subplot()

for i, c  in zip(lines, colors):
    x = np.sin(coords + i)
    y = np.cos(coords + i)
    ax.plot(x * i,
            y * i,
            lw=lw,
            c=c,
            alpha=1/lw)

ax.set_aspect('equal')
ax.axis('off')
plt.show()

