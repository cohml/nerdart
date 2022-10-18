import matplotlib.pyplot as plt
import numpy as np

from nerdart.util.parser import Parser
from nerdart.util.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n = args.n

    x = np.linspace(-np.pi, np.pi, 1000)
    cm_linspace = np.linspace(0, 1, n)
    sin = np.sin(x)

    ax = plt.subplot()
    ax.axis('off')

    ax.bar(x, sin, color=plt.cm.autumn(cm_linspace), alpha=0.25)
    ax.bar(x, -sin, color=plt.cm.rainbow(cm_linspace), alpha=0.25)


def main():
    parser = Parser()
    parser.add('-n', type=int, default=100)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
