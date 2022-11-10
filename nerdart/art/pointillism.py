from argparse import ArgumentTypeError

import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    plots_per_row = args.plots_per_row
    n_dots_per_subplots = args.n_dots_per_subplots
    dot_size = args.dot_size
    alpha = args.alpha

    _, axes = plt.subplots(nrows=plots_per_row, ncols=plots_per_row)
    dot_types = list(".o8Hh")

    for subplot in axes.flat:
        subplot.axis("off")
        for dot in range(20):
            x, y = np.random.random(size=(2, n_dots_per_subplots))
            rgba = np.random.random(4)
            rgba[-1] = alpha
            dot_type = np.random.choice(dot_types)
            subplot.scatter(
                x, y, color=rgba, linewidths=0, s=(20 - dot) * dot_size, marker=dot_type
            )


def alpha_(alpha):
    try:
        alpha = float(alpha)
    except ValueError:
        raise ArgumentTypeError(
            f"Alpha must be a numeric value. Received {type(alpha)}."
        )
    if 0 <= alpha <= 1:
        return float(alpha)
    raise InvalidAlphaError(f"Alpha must be between 0 and 1. Received {alpha}.")


class InvalidAlphaError(Exception):
    """
    Vanilla `ValueError` doesn't show my custom exception message. It just shows
    some `argparse` error text. Not sure why. Anyway, this seems to work instead.
    """

    pass


def main():
    parser = Parser()
    parser.add("-p", "--plots_per_row", type=int, default=4)
    parser.add("-n", "--n_dots_per_subplots", type=int, default=20)
    parser.add("-s", "--dot_size", type=int, default=500)
    parser.add("-a", "--alpha", type=alpha_, default=0.2)
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
