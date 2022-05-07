import matplotlib.pyplot as plt
import numpy as np

from util.parser import Parser
from util.utils import save_or_show, xy


def plot(args):
    bleep = args.bleep
    bloop = args.bloop
    blap = args.blap

    coords = np.linspace(np.pi * bleep, np.pi * bloop, blap)
    x, y = xy(coords)
    colors = plt.cm.prism(np.linspace(0, 1, blap))

    ax = plt.subplot()
    ax.scatter(x * (x + coords), y * (y + coords), c=colors, alpha=0.75)
    ax.set_aspect('equal')
    ax.axis('off')

    save_or_show(args, __file__)


def main():
    parser = Parser()
    parser.add('-e', '--bleep', default=-100, type=int)
    parser.add('-o', '--bloop', default=100, type=int)
    parser.add('-a', '--blap', default=1000, type=int)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
