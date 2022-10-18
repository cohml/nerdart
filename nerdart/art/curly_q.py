import numpy as np
import matplotlib.pyplot as plt

from nerdart.util.parser import Parser
from nerdart.util.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    n = args.n
    width = args.width

    X, Y = xy(np.linspace(-np.pi, np.pi, 50))
    X *= width
    Y *= width

    I = np.linspace(-np.pi * n / 2, np.pi * n / 2, 1000 * n)
    C = plt.cm.gist_rainbow(np.linspace(1, 0, 1000 * n))

    for i, c in zip(I, C):
        x = X + np.sin(i * 2) + i
        y = Y + np.sin(i) * i

        plt.plot(x, y, c=c, alpha=0.5 / n)

    plt.axis('off')


def main():
    parser = Parser()
    parser.add('-n', '--n', type=int, default=10)
    parser.add('-w', '--width', type=int, default=1)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
