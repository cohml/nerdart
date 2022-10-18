import numpy as np
import matplotlib.pyplot as plt

from nerdart.util.parser import Parser
from nerdart.util.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    n_tubes = args.n_tubes
    density = args.density
    length = args.length

    ax = plt.subplot()
    coords = np.linspace(-np.pi, np.pi, 500)
    mod = np.arange(1, n_tubes)[np.newaxis, :]
    y, x = xy(coords)
    x = x[:, np.newaxis] / mod
    y = y[:, np.newaxis] / mod

    for dot in range(density):
        offset = np.random.random() * length

        for xi, yi in zip(x.T, y.T):
            ax.plot(xi + offset, yi - offset, c='k', alpha=0.01, ls=':')

    ax.set_aspect('equal')
    ax.axis('off')


def main():
    parser = Parser()
    parser.add('-n', '--n_tubes', type=int, default=6)
    parser.add('-l', '--length', type=float, default=1)
    parser.add('-d', '--density', type=int, default=2000)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
