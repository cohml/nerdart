import numpy as np
import matplotlib.pyplot as plt

from util.parser import Parser
from util.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n_rectangles = args.n_rectangles

    x = np.random.random(n_rectangles)
    cm = plt.cm.autumn(np.linspace(0, 1, n_rectangles))
    ax = plt.subplot()

    ax.bar(x,
           np.tan(x),
           alpha=0.25,
           color=cm,
           edgecolor='k')
    
    ax.axis('off')


def main():
    parser = Parser()
    parser.add('-n', '--n_rectangles', type=int, default=100)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
