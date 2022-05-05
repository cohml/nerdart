import matplotlib.pyplot as plt
import numpy as np

n = 100
x = np.linspace(-np.pi, np.pi, 1000)
ax = plt.subplot()
ax.axis('off')

ax.bar(x, np.sin(x), alpha=0.25, color=plt.cm.autumn(np.linspace(0,1,n)))
ax.bar(x, -np.sin(x), alpha=0.25, color=plt.cm.rainbow(np.linspace(0,1,n)))

plt.show()
