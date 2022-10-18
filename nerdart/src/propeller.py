import numpy as np
import matplotlib.pyplot as plt

from util.parser import Parser
from util.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n = args.n
    color = args.color
    explode = args.explode
    starriness = args.starriness

    ax = plt.subplot(polar=True)
    x = np.linspace(-np.pi * 1.5, np.pi * 1.5, starriness) * explode

    for i in np.linspace(0, n):
        ax.plot(x + i,
                np.tan(x) * np.sin(x) + i,
                ls=':',
                lw=7,
                alpha=1-i/n,
                color=(1-i/n, 0, i/n) if color else 'k')

    ax.axis('off')


def main():
    parser = Parser()
    parser.add('-n', type=int, default=400)
    parser.add('-c', '--color', action='store_true')
    parser.add('-e', '--explode', type=float, default=1)
    parser.add('-s', '--starriness', type=int, default=10)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
