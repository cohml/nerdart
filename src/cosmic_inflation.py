
import matplotlib.pyplot as plt
import numpy as np

n_lines = 1000
translate = True
striate = True
wormhole = False

samples = np.linspace(0, 10, 1000)
x = np.array([np.sin(i) for i in samples])
y = np.array([np.cos(i) for i in samples])

if wormhole:
    for i in np.linspace(-1, 1, n_lines):
        j = i**i if translate else 0
        rgb = 1-abs(i), abs(i), min(np.random.random(), 0.5) if striate else 0.5
        plt.plot(x*i+j, y*i+j, c=rgb, alpha=1-abs(i)**2)
else:
    for i in np.linspace(-1, 1, n_lines):
        j = i if translate else 0
        rgb = 1-abs(i), abs(i), min(np.random.random(), 0.5) if striate else 0.5
        plt.plot(x*i+j, y*i+j, c=rgb, alpha=max(0.1, 1-abs(i)))

plt.show()
