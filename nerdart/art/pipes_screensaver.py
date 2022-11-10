import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n_pipes = args.n_pipes
    width = args.width

    coords = np.linspace(-np.pi, np.pi, 5 * n_pipes)
    pipe = [np.sin(coords) * width, np.cos(coords) * width]

    for i in range(n_pipes):
        orient = np.random.choice([-1, 1])
        length = np.random.randint(1, 10)
        direction = i % 2

        for j in range(length * width * 2):
            pipe[direction] += orient
            plt.plot(*pipe, c="k", alpha=1 / n_pipes, zorder=i)

    plt.gca().set_aspect("equal")
    plt.tight_layout()
    plt.axis("off")


def main():
    parser = Parser()
    parser.add("-n", "--n_pipes", type=int, default=25)
    parser.add("-w", "--width", type=int, default=10)
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
