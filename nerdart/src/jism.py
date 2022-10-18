import matplotlib.pyplot as plt
import numpy as np

from util.parser import Parser
from util.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n_plots = args.n_plots
    trig = args.trig
    shift = args.shift
    dotted = args.dotted
    base_lw = args.base_lw

    fig, axes = plt.subplots(nrows=n_plots, ncols=n_plots)
    alpha_min = 0.05
    ls = '-'
    if trig:
        trig_coords = np.linspace(0, 10, 100) + np.random.random()

    for i, row in enumerate(axes):
        color = np.random.random(3)
        if i <= n_plots / 2:
            alpha_row = max(2 * i/n_plots, alpha_min)
        else:
            alpha_row = max(2 * (n_plots-i)/n_plots, alpha_min)

        for j, ax in enumerate(row, start=1):
            if dotted:
                ls = '--' if j % 2 == 0 else '-'
            if j <= n_plots / 2:
                scale_factor = j
            else:
                scale_factor = n_plots - j + 1
            alpha_plot = alpha_row * (2 * scale_factor) / n_plots

            if trig:
                x = trig_coords + np.random.random() if shift else trig_coords
                y = np.sin(x * scale_factor)
            else:
                x = np.arange(2)
                y = np.array([0 + scale_factor, 0 - scale_factor])
                if shift:
                    x = x + 0.5 * np.random.random()
            y *= scale_factor

            ax.plot(x, y,
                    ls=ls,
                    color=color,
                    alpha=alpha_plot,
                    lw=base_lw / (n_plots * scale_factor))
            ax.set(ylim=[-5, 5])
            ax.axis('off')


def main():
    parser = Parser()
    parser.add('-n', '--n_plots', type=int, default=11)
    parser.add('-t', '--trig', action='store_false')
    parser.add('-s', '--shift', action='store_true')
    parser.add('-d', '--dotted', action='store_true')
    parser.add('-b', '--base_lw', type=int, default=65)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
