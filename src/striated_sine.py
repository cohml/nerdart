import matplotlib.pyplot as plt
import numpy as np

from random import random

title = 'striated_sinewave.png'
fm = 1 #0.5
sample_rate = 10 # 1000
fade = False

for i in np.linspace(0, 1, 1000):
    x = np.array([np.sin(j * fm) for j in np.linspace(0, 10, sample_rate)])
    am = i if i < 0.5 else 1 - i
    rgb = random(), random(), random()

    if fade:
        a = i if i < 0.5 else 1 - i
    else:
        a = max(0.25, random())

    plt.plot(x * am + i, color=rgb, alpha=a)

plt.axis('off')
plt.tight_layout()
plt.show()
#plt.savefig(title, dpi=600, bbox_inches='tight')
