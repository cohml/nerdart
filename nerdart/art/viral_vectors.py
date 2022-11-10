import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n_dims = args.n_dims
    n_lines = args.n_lines
    linewidth = args.linewidth
    dot_size = args.dot_size

    x = np.arange(n_dims)
    y = np.zeros(x.size)

    for row in x:
        plt.scatter(x, y + row, s=dot_size * 10)

    for line in range(n_lines):
        xi = np.random.choice(x, size=2)
        yi = np.random.choice(x, size=2)
        plt.plot(
            xi,
            yi,
            lw=linewidth,
            marker="o",
            markersize=dot_size,
            markerfacecolor="white",
        )

    plt.axis("off")


def main():
    parser = Parser()
    parser.add("-d", "--n_dims", type=int, default=20)
    parser.add("-l", "--n_lines", type=int, default=10)
    parser.add("-w", "--linewidth", type=float, default=5)
    parser.add("-s", "--dot_size", type=float, default=5)
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
