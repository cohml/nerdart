import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show, xy

SMALLEST_POSSIBLE_ALPHA = 0.0023


@save_or_show(__file__)
def plot(args):
    x = np.linspace(0, 1.2, 1000)
    y, z = xy(x)

    plt.bar(x, y, color="blue", alpha=SMALLEST_POSSIBLE_ALPHA)
    plt.bar(x, z, color="red", alpha=SMALLEST_POSSIBLE_ALPHA)
    plt.axis("off")


def main():
    parser = Parser()
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
