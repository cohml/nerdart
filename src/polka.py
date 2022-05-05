import matplotlib.pyplot as plt
import numpy as np

n_points = 25

x = np.array(list(range(n_points)))
ax = plt.subplot()

for i in range(n_points):
    y = [i] * n_points
    size = np.sin(i) * np.random.random() * 500
#    size = 5000 * (1 - i / n_points)
    ax.scatter(x, y, c='b', alpha=0.5, lw=0, s=size)    # <-- the ValueError is caused by the `size` parameter;
    ax.scatter(x, y, c='r', alpha=0.5, lw=0, s=1-size)  # <-- I've spent a little time debugging but don't quite get it

plt.show()

