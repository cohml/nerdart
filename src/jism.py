import matplotlib.pyplot as plt
import numpy as np
from random import random as r

## params ##
n_plots = 11
trig = True
shift = False
dotted = False
base_lw = 65

def rand_rgb():
  return r(), r(), r()

fig, axes = plt.subplots(nrows=n_plots,
                         ncols=n_plots)

for i, row in enumerate(axes):    # NB: len(axes) == n_plots

  color = rand_rgb()
  alpha_min = 0.05
  alpha_row = (max(2*i/n_plots, alpha_min) if i <= n_plots/2
               else max(2*(n_plots-i)/n_plots, alpha_min))
  
  for j, ax in enumerate(row, start=1):
   
    scale_factor = (j if j <= n_plots/2
                    else n_plots-j+1)
    alpha_plot = alpha_row * (2*scale_factor)/n_plots

    if dotted:
        ls = '--' if j % 2 == 0 else '-'
    else:
        ls = '-'
    
    if trig:
#      x = (np.linspace(0, 10, 100) * scale_factor + r() if shift
#           else np.linspace(0, 10, 100) * scale_factor)
      x = (np.linspace(0, 10, 100) + r() if shift
           else np.linspace(0, 10, 100))
      y = np.array([np.sin(j*scale_factor) for j in x])
    else:
     x = np.array([0, 1]) + r()/2 if shift else np.array([0, 1])
     y = np.array([0+scale_factor, 0-scale_factor])
    
    ax.plot(x,
            y * scale_factor,
            color=color,
            alpha=alpha_plot,
            lw=base_lw/(n_plots*scale_factor),
            ls=ls)
    ax.set(xticks=[], yticks=[], ylim=[-5, 5])
    ax.axis('off')
    
plt.show()
