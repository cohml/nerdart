import matplotlib.pyplot as plt
import numpy as np

n = 100
x = np.random.random(n)
ax = plt.subplot()
ax.axis('off')

ax.bar(x, np.tan(x), alpha=0.25, color=plt.cm.autumn(np.linspace(0,1,n)), edgecolor='k')

plt.show()
