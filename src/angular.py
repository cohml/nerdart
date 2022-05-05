import numpy as np
import matplotlib.pyplot as plt
import random as r

title = 'pastels.png'
slopes = [2, 1, 0, -1, -2]

for slope in slopes:
	
	lines_per_obj = 250
	
	x = [slope]* lines_per_obj
	y = np.array([np.sin(i) for i in np.linspace(0, 10, lines_per_obj)])
	
	rgb = r.random(), r.random(), r.random()
	
	plt.plot((x, y), linewidth=0.8, color=rgb, alpha=1 if slope == 0 else (1.25 - abs(slope/2)))
	
plt.show()
#plt.savefig(title, dpi=600, bbox_inches='tight')
