import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    n_clouds = args.n_clouds
    squiggle = args.squiggle
    n_mountains = args.n_mountains
    mountain_width = args.mountain_width
    mountain_height_min = args.mountain_height_min
    mountain_height_max = args.mountain_height_max
    marker_width = args.marker_width

    fig, ax = plt.subplots()
    fig.tight_layout()

    coords = np.linspace(0, 2 * np.pi, 1000)

    # clouds
    minx = maxx = 0
    for i in range(n_clouds):
        pen_width = abs(np.random.normal(size=coords.size, scale=10)) / 2 * marker_width
        scale = max(0.5, np.random.random())
        n_blobs = np.random.choice([2, 3])

        x_wiggle = np.sin(coords * squiggle / n_blobs) / squiggle * 1.5
        y_wiggle = np.cos(coords * squiggle / n_blobs) / squiggle
        x_translate = np.random.random() * n_clouds * np.random.choice([-1, 1])
        y_translate = 10 + np.random.random() * 2
        x_flip, y_flip = np.random.choice([-1, 1], size=2)

        x = x_wiggle + x_translate + np.sin(coords + x_wiggle * x_flip) * scale * 1.5
        y = y_wiggle + y_translate + np.cos(coords + y_wiggle * y_flip) * scale * 0.75

        ax.scatter(x, y, c="k", s=pen_width, zorder=i + 2)
        ax.fill_between(x, y, color="w", zorder=i + 1, lw=0)

        minx = x.min() if x.min() < minx else minx
        maxx = x.max() if x.max() > maxx else maxx

    # grass
    flowers = plt.cm.prism(np.linspace(0, 1, coords.size))
    np.random.shuffle(flowers)
    grassx = np.linspace(minx, maxx, 1000)
    hills = abs(np.cos(grassx / 3)) / 2
    grassy = np.sin(np.random.random(size=coords.size)) + hills
    ax.fill_between(grassx, grassy, color="g", lw=2, zorder=1000)
    ax.scatter(grassx, grassy, c=flowers, s=5, zorder=1001)

    # sky
    miny = 0
    maxy = 15
    ax.imshow(
        np.linspace(1, 0, 100).reshape(-1, 1),
        extent=[minx, maxx, miny, maxy],
        cmap="Blues",
        zorder=-1,
    )

    # sun
    sunx = np.sin(coords) * 2 + minx
    suny = np.cos(coords) * 2 + maxy
    ax.scatter(sunx, suny, c="k", s=pen_width, zorder=n_clouds + 1)
    ax.fill_between(sunx, suny, color="y", lw=0, zorder=n_clouds)

    # mountains
    n_pts = 5000
    mountcoords = np.linspace(minx, minx + mountain_width, n_pts)
    mount_pen_width = abs(np.random.normal(size=n_pts, loc=2, scale=10)) * marker_width
    colors = plt.cm.Greys(np.linspace(0.25, 0.5, n_mountains))
    for i, c in enumerate(colors):
        i += n_clouds
        height = maxy * np.clip(
            np.random.random(), mountain_height_min, mountain_height_max
        )
        slope = height / (mountcoords[n_pts // 2 - 1] - mountcoords[0])
        mountx = mountcoords + maxx * np.random.random()
        mountainside = (mountx[: n_pts // 2] - mountx[: n_pts // 2].min()) * slope
        mounty = np.array(list(mountainside) + list(mountainside)[::-1])
        ax.scatter(mountx, mounty, c="k", s=mount_pen_width, zorder=i + 2)
        ax.fill_between(mountx, mounty, color=c, zorder=i + 1)

        # snowcap (tall mountains only)
        if height >= maxy * 0.4:
            bottom_y = height * 0.8
            lower_left_corner_xi = abs(mounty - bottom_y).argmin()
            lower_right_corner_xi = mounty.size - lower_left_corner_xi - 1
            lower_left = mountx[lower_left_corner_xi]
            lower_right = mountx[lower_right_corner_xi]
            middle = mountx[mountx.size // 2]
            snowcap_xcoords = [lower_left, middle, lower_right, lower_left]
            snowcap_ycoords = [bottom_y, height, bottom_y, bottom_y]
            ax.scatter(
                np.linspace(lower_left, lower_right, 100),
                np.zeros(100) + bottom_y,
                c="k",
                s=mount_pen_width[:100],
                zorder=i + 2,
            )
            ax.fill(snowcap_xcoords, snowcap_ycoords, c="w", zorder=i + 1)

    ax.set_xlim(minx, maxx)
    ax.set_ylim(miny, maxy)
    ax.axis("off")


def main():
    parser = Parser()
    parser.add("-c", "--n-clouds", type=int, default=8)
    parser.add("-s", "--squiggle", type=int, default=17)
    parser.add("-m", "--n-mountains", type=int, default=5)
    parser.add("-w", "--mountain-width", type=int, default=10)
    parser.add("-i", "--mountain-height-min", type=float, default=0.2)
    parser.add("-x", "--mountain-height-max", type=float, default=0.5)
    parser.add("-d", "--marker-width", type=int, default=1)
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()
