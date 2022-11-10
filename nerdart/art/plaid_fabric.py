import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    density = args.density

    mod = np.linspace(1, 0, 1000)
    lw = 5 * np.random.random(density)

    linspace = np.linspace(-np.pi * 2, np.pi * 2, 1000)
    y = np.sin(linspace) * mod

    ax = plt.subplot()
    ax.axis("off")

    for i in range(density):
        x = linspace + (0.1 * i)
        alpha = 1 - i / density
        ax.plot(x, y, c="k", alpha=alpha, lw=lw[i])


def main():
    parser = Parser()
    parser.add("-d", "--density", type=int, default=100)
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
