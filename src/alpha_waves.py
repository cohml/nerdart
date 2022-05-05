import matplotlib.pyplot as plt
import numpy as np
import sys

if len(sys.argv) < 2:
    n_points = int(input('No. of points to plot: '))
else:
    n_points = int(sys.argv[1])

for j in range(2, 11):

    rgba = np.random.random(), np.random.random(), np.random.random()

    for i in range(n_points):
        x = [np.sin(x) for x in np.linspace(0, 10, n_points)]
        y = [np.cos(y) for y in np.linspace(0, 10, n_points)]

        x = np.array(x)
        y = np.array(y)

        x_colors = [z * i/n_points for z in rgba]
        y_colors = [1 - z for z in x_colors]
        alpha = i/n_points

        plt.plot(x + i/n_points + j, color=x_colors, alpha=alpha if not j % 2 ==0 else 1 - alpha)
#        plt.plot(y + i/n_points + j, color=y_colors, alpha=(1 - alpha))

plt.show()
