import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    n_folds = args.n_folds

    X, Y = xy(np.linspace(-np.pi, np.pi, 8))
    I = np.linspace(0, np.pi * n_folds, 5000)
    C = plt.cm.rainbow(np.linspace(1, 0, 5000))

    for i, c in zip(I, C):
        x = X * np.sin(i) * i + (2 * i)
        y = Y * np.cos(i) * i + (2 * i)
        plt.plot(x, y, c=c, alpha=0.02)

    plt.axis("off")


def main():
    parser = Parser()
    parser.add("-n", "--n-folds", type=int, default=10)
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
