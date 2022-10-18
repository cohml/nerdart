import matplotlib.pyplot as plt
import numpy as np

from nerdart.util.parser import Parser
from nerdart.util.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n_spikes = args.n_spikes
    density = args.density
    seed = args.seed

    rnd = np.random.RandomState(seed)

    slopes = np.linspace(-2, 2, n_spikes)
    y = np.sin(np.linspace(0, 10, density))

    for slope in slopes:
        x = np.ones(density) * slope
        plt.plot((x, y),
                 lw=0.8,
                 color=rnd.random(3),
                 alpha=1 if slope == 0 else abs(slope / 2) / n_spikes)

    plt.axis('off')


def main():
    parser = Parser()
    parser.add('-n', '--n_spikes', type=int, default=5)
    parser.add('-d', '--density', type=int, default=250)
    parser.add('-s', '--seed', type=int, default=5)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
