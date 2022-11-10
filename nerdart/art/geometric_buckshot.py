import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    n_dots = args.n_dots
    density = args.density
    orbitals = args.orbitals
    n_gons = args.n_gons
    linewidth = args.linewidth
    zoom = args.zoom

    nums = np.linspace(-np.pi, np.pi, n_gons + 1)
    dotx, doty = xy(nums)

    ax = plt.subplot()

    for dot in range(n_dots):
        jitterx, jittery = np.random.random(2) * zoom

        for i in np.linspace(1, orbitals, density):
            alpha = np.random.random()
            ax.plot(
                dotx / i + jitterx, doty / i + jittery, lw=linewidth, alpha=alpha, c="k"
            )

    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()


def main():
    parser = Parser()
    parser.add("-n", "--n-dots", type=int, default=50)
    parser.add(
        "-d",
        "--density",
        type=int,
        default=25,
        help="NB: mutually dependent with `orbitals`",
    )
    parser.add(
        "-o",
        "--orbitals",
        type=int,
        default=10,
        help="NB: mutually dependent with `density`",
    )
    parser.add("-g", "--n-gons", type=int, default=4)
    parser.add("-l", "--linewidth", type=float, default=0.25)
    parser.add("-z", "--zoom", type=int, default=5)
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
