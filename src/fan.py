import matplotlib.pyplot as plt
import numpy as np

# params
n_lines = 10
offset = 0 # 1
perspective = False

slopes = np.arange(n_lines)
x = np.array([0, 1])
b = offset

fig, ax = plt.subplots()
for i, m in enumerate(slopes):

    if perspective:
        x = x + 0.1

    line = m*x+b
    lower_bound = slopes[i-1]*x if i != 0 else line

    rgba = (i/n_lines, 1-i/n_lines, 0.5, 0.5)

    if not perspective:
        ax.plot(line, color=rgba[:-1])

    ax.fill_between(x, lower_bound, line, color=rgba)

plt.axis('off')
fig.set_facecolor('k')
plt.show()
