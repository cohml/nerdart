import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    n_shockwaves = args.n_shockwaves
    reverse = args.reverse

    ax = plt.subplot()

    coords = np.logspace(0, 1000, 5000)
    x, y = xy(coords)

    for i in range(n_shockwaves):
        if reverse:
            alpha = (n_shockwaves - i) / n_shockwaves
        else:
            alpha = i / n_shockwaves

        ax.plot(x + i,
                y * i,
                color='k',
                alpha=alpha,
                lw=10)

    ax.axis('off')


def main():
    parser = Parser()
    parser.add('-n', '--n_shockwaves', type=int, default=15)
    parser.add('-r', '--reverse', action='store_true')
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
