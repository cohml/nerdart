import matplotlib.pyplot as plt
import numpy as np

from nerdart.util.parser import Parser
from nerdart.util.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n_twists = args.n_twists

    x = np.linspace(-np.pi * n_twists, np.pi * n_twists, 100)
    c = plt.cm.gist_rainbow(np.linspace(0, 1, x.size))

    for i in np.linspace(0, 10, 100):
        y = np.sin(x + i) + i
        plt.scatter(x, y, alpha=0.2, c=c)

    plt.axis('off')


def main():
    parser = Parser()
    parser.add('-n', '--n_twists', type=int, default=3)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()