import matplotlib.pyplot as plt
import numpy as np

# params
n_floors = 7
circletop = False

ax = plt.subplot()
ax.axis('off')

linspace = np.linspace(-np.pi, np.pi, 1000)
x = np.sin(linspace)
y = np.cos(linspace)

floor_x = x + np.random.random() * 10
floor_x_median = np.median(floor_x) * 10

floor_y = y + np.random.random()
floor_y_median = np.median(floor_y)

if circletop:
    circletop = 0
else:
    circletop = 1

for floor in range(circletop, n_floors + circletop):
    ax.plot([yi - floor if yi > floor_y_median else yi + floor for yi in floor_y],
            [xi + floor if xi > floor_x_median else xi - floor for xi in floor_x],
            color='k')

plt.show()
