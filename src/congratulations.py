import matplotlib.pyplot as plt
import numpy as np

from util.parser import Parser
from util.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n_ribbons = args.n_ribbons
    sparsity = args.sparsity

    coords = np.linspace(0, 1, 100)
    colors = plt.cm.prism(np.linspace(0, 1, n_ribbons))
    x_maxtranslate = y_maxtranslate = 0
    signs = [-1, 1]

    for ribbon, color in zip(range(n_ribbons), colors):

        x_tilt, y_tilt = np.random.random(2)
        x_flip, y_flip = np.random.choice(signs, size=2)
        x_translate, y_translate = np.random.random(2) * sparsity

        x_maxtranslate = x_translate if x_translate > x_maxtranslate else x_maxtranslate
        y_maxtranslate = y_translate if y_translate > y_maxtranslate else y_maxtranslate

        length = np.random.randint(4, 13)
        alpha = np.random.random() ** 2

        for stretch in np.linspace(0, length, 100):

            x = (np.sin(coords + stretch) + stretch * x_tilt) * x_flip + x_translate
            y = (np.cos(coords + stretch) + stretch * y_tilt) * y_flip + y_translate

            plt.plot(x, y, alpha=alpha, color=color)

    plt.xlim(0, x_maxtranslate)
    plt.ylim(0, y_maxtranslate)
    plt.axis('off')


def main():
    parser = Parser()
    parser.add('-n', '--n_ribbons', type=int, default=150)
    parser.add('-s', '--sparsity', type=int, default=100)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
