import matplotlib.pyplot as plt
import numpy as np

from util.parser import Parser
from util.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n_lines = args.n_lines
    max_linewidth = args.max_linewidth

    x = list(range(n_lines))
    y = list(range(n_lines))

    np.random.shuffle(y)

    for i in range(n_lines-1):
        plt.plot([x[i], x[i]],
                 [y[i], y[i+1]],
                 alpha=np.random.random(),
                 lw=max_linewidth*i/n_lines+1)

    plt.axis('off')


def main():
    parser = Parser()
    parser.add('-n', '--n_lines', type=int, default=50)
    parser.add('-m', '--max_linewidth', type=int, default=5)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
