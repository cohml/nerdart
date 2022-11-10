import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    freqmod = args.freqmod
    sample_rate = args.sample_rate
    fade = args.fade

    coords = np.linspace(0, 10, sample_rate)

    for i in np.linspace(0, 1, 1000):
        x = np.sin(coords * freqmod)
        ampmod = i if i < 0.5 else 1 - i
        rgb = np.random.random(3)

        if fade:
            a = i if i < 0.5 else 1 - i
        else:
            a = max(0.25, np.random.random())

        plt.plot(x * ampmod + i, color=rgb, alpha=a)

    plt.axis("off")


def main():
    parser = Parser()
    parser.add("-p", "--freqmod", type=float, default=1)
    parser.add("-s", "--sample_rate", type=int, default=100)
    parser.add("-f", "--fade", action="store_true")
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
