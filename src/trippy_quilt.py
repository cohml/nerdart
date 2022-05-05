import numpy as np
import matplotlib.pyplot as plt
import random as r

title = 'striated_sinewave_manyCycles_v2.png'
fm = 50

for i in np.linspace(0, 1, 500):
	
	x = np.array([np.sin(j * fm) for j in np.linspace(0, 10, 800)])
	
	am = i if i < 0.5 else 1 - i
	
	rgba = r.random(), r.random(), r.random(), max(r.random(), 0.25)
	
	plt.plot(x * am + i, color=rgba)

plt.show()
#plt.savefig(title, dpi=600, bbox_inches='tight')



