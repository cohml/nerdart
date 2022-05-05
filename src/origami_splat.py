import numpy as np
import matplotlib.pyplot as plt

n_lines = 100
fade = True

mod = np.linspace(-1, 1, n_lines)
x = np.array([np.absolute(np.sin(i)) for i in range(n_lines)])
y = mod * 10

for i in range(n_lines):
	plt.plot(x*mod[i], y*mod[i],
					 c=(i/n_lines, 0.2, 1-i/n_lines),
					 lw=(2-2*np.absolute(mod[i])) if fade else 1)

plt.show()

