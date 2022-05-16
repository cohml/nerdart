import matplotlib.pyplot as plt
import numpy as np

from argparse import ArgumentTypeError

from util.parser import Parser
from util.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    roundness = args.roundness
    width = args.width
    shrinkray = args.shrinkray
    threshold = args.threshold
    nrows = args.nrows
    ncols = args.ncols

    coords = np.linspace(-np.pi, np.pi, roundness) + np.pi / 4
    x, y = xy(coords)
    x /= shrinkray
    y /= shrinkray

    ax = plt.subplot(aspect='equal')
    ax.axis('off')

    for row in range(nrows):
        for col in range(ncols):
            odds = col / ncols + np.random.random() ** 2
            ax.plot(col + x + odds * (odds > threshold),
                    row + y + odds * (odds > threshold),
                    lw=width * (ncols - col) / ncols,
                    c='k')


def probability(threshold) -> float:
    """
    The probability of any individal "pixel" being perturbed off the grid-like pattern,
    which is modulated by the `threshold` option. This function simply enforces that
    the passed option be a number between 0 and 1, inclusive.
    """

    try:
        threshold = float(threshold)
    except ValueError:
        err = f'The threshold must be a numeric value. Received {type(threshold)}.'
        raise ArgumentTypeError(err)

    if not (0 <= threshold <= 1):
        err = f'The threshold must be between 0 and 1, inclusive. Received {threshold}.'
        raise ArgumentTypeError(err)

    return threshold


def main():
    parser = Parser()
    parser.add('-o', '--roundness', type=int, default=5)
    parser.add('-w', '--width', type=float, default=1.5)
    parser.add('-s', '--shrinkray', type=int, default=3)
    parser.add('-t', '--threshold', type=probability, default=1)
    parser.add('-r', '--nrows', type=int, default=100)
    parser.add('-c', '--ncols', type=int, default=100)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
