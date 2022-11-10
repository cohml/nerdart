import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    n_lines = args.n_lines
    translate = args.translate
    striate = args.striate
    wormhole = args.wormhole

    x, y = xy(np.linspace(0, 10, 1000))

    if wormhole:
        for i in np.linspace(-1, 1, n_lines):
            j = i**i if translate else 0
            rgb = 1 - abs(i), abs(i), min(np.random.random(), 0.5) if striate else 0.5
            plt.plot(x * i + j, y * i + j, c=rgb, alpha=1 - abs(i) ** 2)

    else:
        for i in np.linspace(-1, 1, n_lines):
            j = i if translate else 0
            rgb = 1 - abs(i), abs(i), min(np.random.random(), 0.5) if striate else 0.5
            plt.plot(x * i + j, y * i + j, c=rgb, alpha=max(0.1, 1 - abs(i)))

    plt.axis("off")


def main():
    parser = Parser()
    parser.add("-n", "--n-lines", type=int, default=1000)
    parser.add("-t", "--translate", action="store_true")
    parser.add("-s", "--striate", action="store_true")
    parser.add("-w", "--wormhole", action="store_true")
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
