import numpy as np
import matplotlib.pyplot as plt

from nerdart.util.parser import Parser
from nerdart.util.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    freqmod = args.freqmod
    density = args.density

    ax = plt.subplot()
    coords = np.linspace(0, 10, 800)
    x = np.sin(coords * freqmod)

    for i in np.linspace(0, 1, density):
        ampmod = i if i < 0.5 else 1 - i
        rgb = np.random.random(3)
        a = max(np.random.random(), 0.25)
        ax.plot(x * ampmod + i, color=rgb, alpha=a)

    ax.axis('off')


def main():
    parser = Parser()
    parser.add('-f', '--freqmod', type=float, default=50.0)
    parser.add('-d', '--density', type=int, default=500)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
