import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    density = args.density
    points = args.points

    coords = np.linspace(1, 1000, 100)
    x, y = xy(coords)

    if points:
        plot = plt.scatter
    else:
        plot = plt.plot

    for i in range(density):
        plot(x * i, y * i, alpha=i / density, color="k", lw=0.5)

    plt.gca().set_aspect("equal")
    plt.axis("off")


def main():
    parser = Parser()
    parser.add("-d", "--density", type=int, default=15)
    parser.add("-p", "--points", action="store_true")
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
