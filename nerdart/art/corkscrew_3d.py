import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    length = args.length

    x = np.linspace(-np.pi * length, np.pi * length, 1000 * length)
    y, z = xy(x)

    ax = plt.subplot(projection='3d')
    ax.bar(x, y, z, color=plt.cm.gist_rainbow(np.linspace(0, 1, x.size)))
    ax.axis('off')


def main():
    parser = Parser()
    parser.add('-l', '--length', type=int, default=3)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
