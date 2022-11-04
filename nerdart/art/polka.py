import matplotlib.pyplot as plt
import numpy as np

from scipy.signal import sawtooth

from nerdart import Parser
from nerdart.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n_points = args.n_points
    n_waves = args.n_waves
    scale_factor = args.scale_factor
    tilt_factor = args.tilt_factor

    points = np.arange(n_points)
    x = points.copy()
    y = np.zeros(n_points)

    for point in points:
        xi = x + point * tilt_factor
        y[:] = point

        size = 0.5 * sawtooth(2 * np.pi * n_waves * (point/n_points), 0.5) + 0.5
        size *= scale_factor

        plt.scatter(xi, y, c='red',  alpha=0.4, lw=0, s=size)
        plt.scatter(xi, y, c='blue', alpha=0.4, lw=0, s=scale_factor - size)

    if tilt_factor >= 0:
        plt.xlim(0, tilt_factor * n_points - tilt_factor + n_points - 1)
    else:
        plt.xlim(tilt_factor * n_points - tilt_factor, n_points - 1)
    plt.ylim(0, n_points - 1)
    plt.axis('off')


def main():
    parser = Parser()
    parser.add('-p', '--n_points', type=int, default=25)
    parser.add('-w', '--n_waves', type=int, default=3)
    parser.add('-s', '--scale_factor', type=float, default=500)
    parser.add('-t', '--tilt_factor', type=float, default=0)
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
