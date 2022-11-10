import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    n_floors = args.n_floors
    circletop = args.circletop

    ax = plt.subplot(aspect="equal")
    ax.axis("off")

    x, y = xy(np.linspace(-np.pi, np.pi, 1000))

    floor_x = x + np.random.random() * 10
    floor_x_median = np.median(floor_x) * 10

    floor_y = y + np.random.random()
    floor_y_median = np.median(floor_y)

    circletop = int(not circletop)

    for floor in range(circletop, n_floors + circletop):
        ax.plot(
            [yi - floor if yi > floor_y_median else yi + floor for yi in floor_y],
            [xi + floor if xi > floor_x_median else xi - floor for xi in floor_x],
            color="k",
        )


def main():
    parser = Parser()
    parser.add("-n", "--n-floors", type=int, default=7)
    parser.add("-c", "--circletop", action="store_true")
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
