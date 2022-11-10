import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show, xy


@save_or_show(__file__)
def plot(args):
    num_points = args.num_points
    sunny = args.sunny

    coords = np.linspace(0, 10, num_points)
    x, y = xy(coords)

    for i in range(2, 11):
        rgb = np.random.random(3)

        for j in range(num_points):
            x_colors = rgb * (j / num_points)
            y_colors = 1 - x_colors
            alpha = j / num_points

            if sunny:
                arr = y + i + (j / num_points)
                color = y_colors
                alpha = 1 - alpha
            else:
                arr = x + i + (j / num_points)
                color = x_colors
                alpha = 1 - alpha if i % 2 == 0 else alpha

            plt.plot(arr, color=color, alpha=alpha)
            plt.axis("off")


def main():
    parser = Parser()
    parser.add("-n", "--num-points", type=int, default=50)
    parser.add("-s", "--sunny", action="store_true")
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
