import matplotlib.pyplot as plt
import numpy as np

from util.parser import Parser
from util.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    n_polygons = args.n_polygons
    roundness = args.roundness
    cmap = args.cmap

    x, y = xy(np.linspace(-np.pi, np.pi, roundness))

    offsets = np.linspace(-np.pi, np.pi, n_polygons)
    colors = getattr(plt.cm, cmap)(np.linspace(0, 1, n_polygons))

    ax = plt.subplot(aspect='equal')
    ax.axis('off')

    for i, c in zip(offsets, colors):
        xi = x + np.sin(i)/2
        yi = y - np.cos(i)/2
        ax.fill_between(xi, yi,
                        color=c,
                        zorder=-i,
                        linewidth=0,
                        alpha=4/n_polygons)

    ets_labs = 'ETS' + ' ' * 10 + 'LABS'
    ai = r'$\bfAI$'
    for text, color, x in [(ets_labs, 'k', 0.4), (ai, 'w', -0.1)]:
        ax.annotate(text, (x, 0), c=color, fontsize=100, fontname='Lucida Grande',
                    ha='center', va='center', zorder=n_polygons + 1)


def main():
    parser = Parser()
    parser.add('-n', '--n_polygons', type=int, default=8)
    parser.add('-r', '--roundness', type=int, default=100)
    parser.add('-c', '--cmap', type=str, default='viridis')
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
