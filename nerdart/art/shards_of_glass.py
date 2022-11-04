import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n_shapes = args.n_shapes
    n_angles = args.n_angles
    density = args.density

    coords = np.linspace(-np.pi, np.pi, n_angles + 1)
    ndims = int(np.ceil(np.sqrt(n_shapes)))
    dims = range(density, ndims + density)
    ax = plt.subplot(polar=False)

    for row in dims:
        for col in dims:
            I = np.linspace(0, 2 * np.pi, row)
            C = plt.cm.autumn(np.linspace(0, 1, I.size))

            for i, c in zip(I, C):
                x = np.sin(coords + i + row) + i + row * 4 + np.random.random()
                y = np.cos(coords + i + col) + i + col * 4 + np.random.random()
                a = np.clip(1 - i / I.max(), 0.2, 1)
                c[-1] = a

                ax.plot(x, y, lw=1, c=c, zorder=col)
                ax.fill(x, y, color=c)

    ax.axis('off')


def main():
    parser = Parser()
    parser.add('-n', '--n_shapes', type=int, default=25)
    parser.add('-a', '--n_angles', type=int, default=3)
    parser.add('-d', '--density', type=int, default=3)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
