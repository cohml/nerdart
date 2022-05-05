import matplotlib.pyplot as plt
import numpy as np

# params
density = 1000
n_cycles = 3
resolution = 1000
fade = False
colors = 'rainbow' # choose btw 'rainbow' or 'RAINBOW'

x = np.linspace(0, n_cycles * 2 * np.pi, resolution)
y = np.sin(x)
colors = {'rainbow' : plt.cm.rainbow,
          'RAINBOW' : plt.cm.gist_rainbow}.get(colors)

offsets = np.linspace(-1, 1, density)
colors = colors((offsets + 1) / 2)

ax = plt.subplot()
ax.axis('off')

for offset, color in zip(offsets, colors[::-1]):
    mod = 1 - abs(offset)
    ax.plot(x,
            y * mod + offset,
            color=color,
            alpha=mod if fade else 1,
            ls='-.')

plt.tight_layout()
plt.show()
