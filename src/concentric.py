import matplotlib.pyplot as plt
import numpy as np
from random import random as r

## params ##
u = 10
v = 100
n_circles = 1000
rubber_band_ball = False

def data(func):
    return np.array([func(i) for i in np.linspace(0, u, v)])

x = data(np.cos)
y = data(np.sin)

fig, ax = plt.subplots()

for i in range(n_circles):

    jitter = r()

    plt.plot(x * r() if rubber_band_ball else x * jitter,
             y * r() if rubber_band_ball else y * jitter,
             alpha=jitter**1/2)
#             color='r')

ax.axis('off')

plt.show()
