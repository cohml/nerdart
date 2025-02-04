import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    n_angles = args.n_angles
    n_objects = args.n_objects
    width = args.width
    shift = args.shift
    colorful = args.colorful

    coords = np.linspace(-np.pi, np.pi, n_angles + 1)
    x = np.tile(np.sin(coords), (n_objects, 1)) * np.arange(1, n_objects + 1).reshape(n_objects, 1)
    y = np.tile(-np.cos(coords), (n_objects, 1)) * np.arange(1, n_objects + 1).reshape(n_objects, 1)
    if colorful:
        cm = plt.cm.Dark2(np.linspace(0, 1, n_objects))
    else:
        cm = "k" * n_objects

    ax = plt.subplot()
    ax.plot(x[0], y[0], lw=width, c=cm[0], solid_capstyle="round")
    for i in range(1, n_objects):
        shift_x = x[i][i % n_angles] - x[i - 1][i % n_angles]
        shift_y = y[i][i % n_angles] - y[i - 1][i % n_angles]
        x[i] -= shift_x * shift
        y[i] -= shift_y * shift
        plt.plot(
            x[i],
            y[i],
            c=cm[i],
            lw=width,
            solid_capstyle="round",
            alpha=2/3 if colorful else 1,
        )

    ax.set_aspect("equal")
    ax.axis("off")


def main():
    parser = Parser()
    parser.add("-a", "--n-angles", type=int, default=3)
    parser.add("-o", "--n-objects", type=int, default=25)
    parser.add("-w", "--width", type=int, default=10)
    parser.add("-s", "--shift", type=float, default=1.0)  # super, super, super sensitive
    parser.add("-c", "--colorful", action="store_true")
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
