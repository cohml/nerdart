import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    init_x = args.init_x
    init_y = args.init_y
    n_squares = args.n_squares
    n_floors = args.n_floors

    coords = [
        [init_x, init_x, init_x, init_y, init_y, init_y, init_y, init_x],
        [init_x, init_y, init_y, init_y, init_y, init_x, init_x, init_x],
    ]
    x, y = map(np.array, coords)
    mod = np.linspace(-np.pi, np.pi, n_squares)
    cm = plt.cm.Spectral(np.linspace(0, 1, n_squares))
    ax = plt.subplot()

    for c, m in zip(cm, mod):
        plt.plot(x + np.sin(m * n_floors), y + np.cos(m), alpha=0.2, lw=10, c=c)

    ax.set_aspect("equal")
    ax.axis("off")


def main():
    parser = Parser()
    parser.add("-x", "--init-x", type=float, default=0)
    parser.add("-y", "--init-y", type=float, default=1)
    parser.add("-s", "--n-squares", type=int, default=500)
    parser.add("-f", "--n-floors", type=int, default=5)
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
