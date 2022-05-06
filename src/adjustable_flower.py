import matplotlib.pyplot as plt
import numpy as np

from utils.defaults import DEFAULTS
from utils.parser import Parser


def plot(args):
    bleep = args.bleep
    bloop = args.bloop
    blap = args.blap

    coords = np.linspace(np.pi * bleep, np.pi * bloop, blap)
    x = np.sin(coords)
    y = np.cos(coords)
    colors = plt.cm.prism(np.linspace(0, 1, blap))

    ax = plt.subplot()
    ax.scatter(x * (x + coords), y * (y + coords), c=colors, alpha=0.75)
    ax.set_aspect('equal')
    ax.axis('off')

    if args.save_image is None:
        plt.show()
    else:
        save_path = args.save_image or DEFAULTS['IMG_DIR'] / __file__
        print(save_path)
        # plt.savefig

def main():
    parser = Parser()
    parser.add(
        '-e', '--bleep',
        default=-100,
        type=int,
        help='...'
    )
    parser.add(
        '-o', '--bloop',
        default=100,
        type=int,
        help='...'
    )
    parser.add(
        '-a', '--blap',
        default=1000,
        type=int,
        help='...'
    )
    args = parser.parse()

    plot(args)


if __name__ == '__main__':
    main()
