import numpy as np
import matplotlib.pyplot as plt
import random as r

plots_per_row = 4
blurry_vision = True

title = 'pointillism.png'

for subplot in range(1, plots_per_row**2+1):
    plt.subplot(plots_per_row, plots_per_row, subplot)
    #for i in range(1, 300, 5):
    for i in reversed(list(range(0, 10001, 500))):
        m = lambda x: max(r.random(), 0.3)
        n_dots = 20
        x = [r.random() for j in range(n_dots)]
        y = [r.random() for k in range(n_dots)]
        #rgba = r.random(), r.random(), r.random(), max(r.random(), 0.25)
        rgba = r.random(), r.random(), r.random(), 0.2
        plt.scatter(x, y, s=i, color=rgba, linewidths=0,
                    marker=r.choice(['.', 'o', '8', 'H', 'h']))

    plt.axis('off')

    if blurry_vision:
        plt.xlim((0,1))
        plt.ylim((0,1))

plt.show()

#plt.savefig(title, dpi=600, bbox_inches='tight')
