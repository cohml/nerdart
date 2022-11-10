import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    n_elbows = args.n_elbows
    n_cycles = args.n_cycles
    line_width = args.line_width
    spacing = args.spacing
    three_d_amount = args.three_d_amount

    coords = np.linspace(0, 2 * np.pi * n_cycles, n_elbows)
    spiralizer = np.linspace(0, spacing, n_elbows)
    x, y = xy(coords)
    lims = (-5, 5)

    three_d_offsets = [0] + ([three_d_amount] if three_d_amount != 0 else [])

    for three_d_offset in three_d_offsets:
        plt.plot(
            x * spiralizer + three_d_offset,
            y * spiralizer + three_d_offset,
            lw=line_width,
        )

    plt.gca().set_aspect("equal")
    plt.xlim(lims)
    plt.ylim(lims)
    plt.axis("off")


def main():
    parser = Parser()
    parser.add("-e", "--n-elbows", type=int, default=1000)
    parser.add("-c", "--n-cycles", type=int, default=100)
    parser.add("-s", "--spacing", type=int, default=5)
    parser.add("-w", "--line-width", type=float, default=1.0)
    parser.add("-d", "--three-d-amount", type=float, default=0)
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
