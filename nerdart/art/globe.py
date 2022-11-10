import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    minimalize = args.minimalize
    n = args.n

    ax = plt.subplot(polar=minimalize)
    ax.axis("off")

    coords = np.logspace(0, 1000, 100)
    x, y = xy(coords)

    for i in range(n):
        ax.plot(y * i, x * i * coords, color="k", alpha=i / n)


def main():
    parser = Parser()
    parser.add("-n", type=int, default=15)
    parser.add("-m", "--minimalize", action="store_true")
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
