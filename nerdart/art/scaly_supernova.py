from argparse import ArgumentTypeError

import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n_circles = args.n_circles
    n_dots_per_circle = args.n_dots_per_circle
    base_size = args.base_size
    offset = args.offset
    alpha = args.alpha
    spiral = args.spiral

    ax = plt.subplot()

    if spiral:

        n = n_circles * n_dots_per_circle
        offsets = np.zeros(n)
        offsets[::2] = offset
        coords = np.linspace(0, np.pi * n_circles, n) + offsets
        radius_multipliers = np.linspace(0, 15, n)
        cm = plt.cm.brg(np.linspace(1, 0, n))

        ax.scatter(
            np.sin(coords) * radius_multipliers,
            np.cos(coords) * radius_multipliers,
            s=base_size * radius_multipliers,
            alpha=alpha,
            color=cm,
        )

    else:

        coords = np.linspace(-np.pi, np.pi, n_dots_per_circle)
        radius_multipliers = np.linspace(0, 15, n_circles)
        cm = plt.cm.brg(np.linspace(1, 0, n_circles))

        for i, (c, radius_multiplier) in enumerate(zip(cm, radius_multipliers)):
            icoords = coords + (0 if i % 2 == 0 else offset)
            x = np.sin(icoords) * radius_multiplier
            y = np.cos(icoords) * radius_multiplier

            ax.scatter(x, y, s=base_size * radius_multiplier * i, alpha=alpha, color=c)

        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)

    ax.set_aspect("equal")
    ax.axis("off")


def alpha_(value) -> float:
    """
    Transparency of individual dots, where 0 is invisible and 1 is opaque.

    This function simply enforces that the passed option be a number between 0
    and 1, inclusive.
    """

    try:
        value = float(value)
    except ValueError:
        err = f"The value must be a numeric value. Received {type(value)}."
        raise ArgumentTypeError(err)

    if not (0 <= value <= 1):
        err = f"The value must be between 0 and 1, inclusive. Received {value}."
        raise ArgumentTypeError(err)

    return value


def main():
    parser = Parser()
    parser.add("-c", "--n-circles", type=int, default=50)
    parser.add("-d", "--n-dots-per-circle", type=int, default=20)
    parser.add("-s", "--base-size", type=int, default=20)
    parser.add("-o", "--offset", type=float, default=np.pi)
    parser.add("-a", "--alpha", type=alpha_, default=1)
    parser.add("-p", "--spiral", action="store_true")
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
