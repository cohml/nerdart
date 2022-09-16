import matplotlib.pyplot as plt
import numpy as np

from util.parser import Parser
from util.utils import save_or_show, xy

@save_or_show(__file__)
def plot(args):
    u = args.u
    v = args.v
    width = args.width
    color = args.color
    jitter = args.jitter
    n_circles = args.n_circles
    rubber_band_ball = args.rubber_band_ball

    coords = np.linspace(0, u, v)
    x, y = xy(coords)
    ax = plt.subplot(aspect='equal')
    ax.axis('off')

    for i in np.linspace(10 * -np.pi, 10 * np.pi, n_circles):
        jitter = (np.random.random() if jitter else i / n_circles) ** 0.5
        lw = width or (jitter if rubber_band_ball else i/n_circles)

        ax.plot(x * (np.random.random() if rubber_band_ball else jitter),
                y * (np.random.random() if rubber_band_ball else jitter),
                alpha=jitter,
                color=color,
                lw=lw)


def main():
    parser = Parser()
    parser.add('-u', '--u', type=int, default=10)
    parser.add('-v', '--v', type=int, default=100)
    parser.add('-w', '--width', type=int)
    parser.add('-c', '--color', type=str, default='black')
    parser.add('-j', '--jitter', action='store_true')
    parser.add('-n', '--n_circles', type=int, default=1000)
    parser.add('-r', '--rubber_band_ball', action='store_true')
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
