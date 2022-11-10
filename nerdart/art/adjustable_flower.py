import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    bleep = args.bleep
    bloop = args.bloop
    blap = args.blap
    size = args.size

    coords = np.linspace(np.pi * bleep, np.pi * bloop, blap)
    x, y = xy(coords)
    colors = plt.cm.prism(np.linspace(0, 1, blap))

    ax = plt.subplot()
    ax.scatter(x * (x + coords), y * (y + coords), c=colors, alpha=0.75, s=size)
    ax.set_aspect("equal")
    ax.axis("off")


def main():
    parser = Parser()
    parser.add("-e", "--bleep", type=int, default=-100)
    parser.add("-o", "--bloop", type=int, default=100)
    parser.add("-a", "--blap", type=int, default=1000)
    parser.add("-s", "--size", type=int, default=20)
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
