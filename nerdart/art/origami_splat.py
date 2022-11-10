import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n_lines = args.n_lines
    fade = args.fade

    mod = np.linspace(-1, 1, n_lines)
    if fade:
        lw = 2 - 2 * abs(mod)
    else:
        lw = [1] * n_lines

    x = abs(np.sin(np.arange(n_lines)))
    y = mod * 10

    for i in range(n_lines):
        c = (i / n_lines, 1 / 5, 1 - i / n_lines)
        plt.plot(x * mod[i], y * mod[i], lw=lw[i], c=c)

    plt.axis("off")


def main():
    parser = Parser()
    parser.add("-n", "--n_lines", type=int, default=100)
    parser.add("-f", "--fade", action="store_true")
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
