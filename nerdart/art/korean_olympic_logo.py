import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    swirls = args.swirls
    sparsity = args.sparsity
    thickness = args.thickness

    coords = np.linspace(0, 1, 10)
    lines = np.linspace(-10 * sparsity, 10 * swirls, 100 * swirls)
    lines_normed = (lines - lines.min())/np.ptp(lines) # squash b/w 0 and 1 for cm
    colors = plt.cm.gist_rainbow(lines_normed)
    lw = max(0, np.log10(thickness)) + 1e-10

    ax = plt.subplot()

    for i, c  in zip(lines, colors):
        x = np.sin(coords + i)
        y = np.cos(coords + i)
        ax.plot(x * i,
                y * i,
                lw=lw,
                c=c,
                alpha=1/lw)

    ax.set_aspect('equal')
    ax.axis('off')


def main():
    parser = Parser()
    parser.add('-w', '--swirls', type=int, default=1)
    parser.add('-p', '--sparsity', type=int, default=1)
    parser.add('-t', '--thickness', type=int, default=10)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
