import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show

COLORS = {
    "rainbow": plt.cm.rainbow,
    "gist_rainbow": plt.cm.gist_rainbow,
    "plasma": plt.cm.plasma,
    "viridis": plt.cm.viridis,
}


@save_or_show(__file__)
def plot(args):
    n_periods = args.n_periods
    density = args.density
    resolution = args.resolution
    colors = COLORS[args.color]
    fade = args.fade

    x = np.linspace(0, n_periods * 2 * np.pi, resolution)
    y = np.sin(x)

    offsets = np.linspace(-1, 1, density)
    colors = colors((offsets + 1) / 2)

    for offset, color in zip(offsets, colors[::-1]):
        mod = 1 - abs(offset)
        plt.plot(
            x, y * mod + offset, alpha=mod if fade else 1, color=color, linestyle="-."
        )

    plt.axis("off")


def main():
    parser = Parser()
    parser.add("-n", "--n_periods", type=int, default=3)
    parser.add("-d", "--density", type=int, default=1000)
    parser.add("-r", "--resolution", type=int, default=200)
    parser.add("-c", "--color", choices=COLORS.keys(), default="rainbow")
    parser.add("-f", "--fade", action="store_true")
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
