import matplotlib.pyplot as plt
import numpy as np

from util.parser import Parser
from util.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n_star_trails = args.n_star_trails
    offset = args.offset

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


def main():
    parser = Parser()
    parser.add('-n', '--n_star_trails', type=int, default=5000)
    parser.add('-o', '--offset', type=float, default=0.1)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
