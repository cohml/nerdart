import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    squishification = args.squishification
    resolution = args.resolution
    incl_dashdot = args.incl_dashdot

    linestyles = ['-', ':', '--'] + (['-.'] if incl_dashdot else [])
    coords = np.linspace(0, 2 * np.pi, resolution)
    _, axes = plt.subplots(nrows=len(linestyles))

    for i in np.linspace(0, squishification, resolution):
        for ax, ls in zip(axes, linestyles):
            color = (i / squishification, 0, 1 - (i / squishification))
            ax.axis('off')
            ax.plot(coords + (0.5 * i),
                    np.sin(coords),
                    ls=ls,
                    color=color,
                    alpha=0.15)


def main():
    parser = Parser()
    parser.add('-s', '--squishification', type=int, default=10)
    parser.add('-r', '--resolution', type=int, default=1000)
    parser.add('-i', '--incl_dashdot', action='store_true')
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
