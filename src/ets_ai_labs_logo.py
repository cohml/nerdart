import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# params
n_polygons = None or 8
roundness = None or 100
cmap = None or 'viridis'

home = Path.home()
coords = np.linspace(-np.pi, np.pi, roundness)
x = np.sin(coords)
y = np.cos(coords)

offsets = np.linspace(-np.pi, np.pi, n_polygons)
colors = getattr(plt.cm, cmap)(np.linspace(0, 1, n_polygons))

ax = plt.subplot(aspect='equal')
ax.axis('off')

for i, c in zip(offsets, colors):
    xi = x + np.sin(i)/2
    yi = y - np.cos(i)/2
    ax.fill_between(xi, yi,
                    color=c,
                    zorder=-i,
                    linewidth=0,
                    alpha=4/n_polygons)

ets_labs = 'ETS' + ' ' * 10 + 'LABS'
ai = r'$\bfAI$'
for text, color, x in [(ets_labs, 'k', 0.4), (ai, 'w', -0.1)]:
    ax.annotate(text, (x, 0), c=color, fontsize=100, fontname='Lucida Grande',
                ha='center', va='center', zorder=n_polygons + 1)

plt.savefig(home / 'ets_ai_labs.png', dpi=150, bbox_inches='tight')
#plt.show()
