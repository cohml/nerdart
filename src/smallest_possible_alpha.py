import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,1.2,1000)
y = np.sin(x)
z = np.cos(x)
plt.bar(x,y,color='blue',alpha=2e-3)
plt.bar(x,z,color='red',alpha=2e-3)
plt.axis('off')
plt.tight_layout()
plt.show()

