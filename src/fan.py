import matplotlib.pyplot as plt
import numpy as np

from util.parser import Parser
from util.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n_lines = args.n_lines
    offset = args.offset
    perspective = args.perspective

    slopes = np.arange(n_lines)
    x = np.array([0, 1])
    b = offset

    fig, ax = plt.subplots()
    fig.set_facecolor('k')
    ax.axis('off')

    for i, m in enumerate(slopes):

        if perspective:
            x = x + 0.1

        line = m*x+b
        lower_bound = slopes[i-1]*x if i != 0 else line

        rgba = (i/n_lines, 1-i/n_lines, 0.5, 0.5)

        if not perspective:
            ax.plot(line, color=rgba[:-1])

        ax.fill_between(x, lower_bound, line, color=rgba)


def main():
    parser = Parser()
    parser.add('-n', '--n_lines', type=int, default=10)
    parser.add('-o', '--offset', type=int, default=0)
    parser.add('-p', '--perspective', action='store_true')
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
