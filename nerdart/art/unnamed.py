import numpy as np
import matplotlib.pyplot as plt

from argparse import ArgumentTypeError

from nerdart.util.parser import Parser
from nerdart.util.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    n_rings = args.n_rings
    shakiness = args.shakiness

    if shakiness < 1:
        raise ArgumentTypeError(
            '`shakiness` must be greater than or equal to 1; '
            f'got {shakiness}'
        )

    ax = plt.subplot()
    coords = np.linspace(-np.pi, np.pi, 100)
    x, y = xy(coords)

    for blur in range(shakiness):
        ring_x = x + np.random.random()
        ring_y = y + np.random.random()

        gt_median_x = ring_x > np.median(ring_x)
        gt_median_y = ring_y > np.median(ring_y)

        for ring in range(1, n_rings + 1):
            ax.plot(np.where(gt_median_x, ring_x + ring, ring_x - ring),
                    np.where(gt_median_y, ring_y + ring, ring_y - ring),
                    lw=(10 / shakiness) * ring / n_rings,
                    color='k')

    plt.axis('off')


def main():
    parser = Parser()
    parser.add('-n', '--n_rings', type=int, default=30)
    parser.add('-s', '--shakiness', type=int, default=1)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
