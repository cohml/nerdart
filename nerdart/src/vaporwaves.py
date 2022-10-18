import numpy as np
import matplotlib.pyplot as plt

from argparse import ArgumentTypeError

from util.parser import Parser
from util.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n_waves = args.n_waves

    if (n_waves == 0) or (n_waves % 200 != 0):
        raise ArgumentTypeError(
            '`n_waves` must be a positive (nonzero) multiple of 200; '
            f'got {n_waves}'
        )

    for j in (1, -1):
        for i in range(0, n_waves, 200):
            for si in range(-i, i):
                color = abs(si / n_waves), 0, 1 - abs(si / n_waves)
                x = np.linspace(-np.pi * 1.5, np.pi * 1.5, abs(si))
                y = si + i + (np.sin(x) * si)
                x *= j
                plt.plot(x,
                         y,
                         lw=0.1,
                         zorder=-i,
                         color=color,
                         alpha=color[0])

    plt.axis('off')


def main():
    parser = Parser()
    parser.add('-n', '--n_waves', type=int, default=1000)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
