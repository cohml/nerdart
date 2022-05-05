import matplotlib.pyplot as plt
import numpy as np

# params
n_star_trails = 5000
offset = 0.1

fig, ax = plt.subplots()
fig.tight_layout(pad=-25)

# plot star trails
lengths = np.linspace(0, 0.25, 6)
weights = np.linspace(1/3, 0, 6)
for i in range(n_star_trails):
    trail_length = np.random.choice(lengths, p=weights)
    trail_coords = np.linspace(0, trail_length, 10)
    jitter = np.random.random()

    star_x = np.sin(trail_coords + jitter * i) * jitter + offset
    star_y = np.cos(trail_coords + jitter * i) * jitter + offset
    ax.plot(star_x, star_y,
            c='lightgrey',
            lw=np.random.random() ** 2,
            alpha=np.random.random() ** 2)

# set gradient color of sky
ax.imshow(np.linspace(0, 1, 1000).reshape(-1, 1) ** 4,
          extent=[-1, 1] * 2,
          cmap='bone')

ax.set_aspect('equal')
ax.axis('off')
plt.show()
