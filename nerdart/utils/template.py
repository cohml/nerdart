from nerdart import DEFAULTS

TEMPLATE = """

import matplotlib.pyplot as plt
import numpy as np

from nerdart import Parser
from nerdart.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    # insert one line per command line argument below, using the following format
    foo = args.foo

    # insert nerdy nuts and artistic bolts below
    pass


def main():
    parser = Parser()
    # insert one line per command line argument below; supply `type` and `default`
    parser.add("-f", "--foo", type=..., default=...)
    args = parser.parse()
    plot(args)


if __name__ == "__main__":
    main()

"""


class Template:
    def __init__(self, name):
        self.name = name
        self.template = TEMPLATE.strip()

    def generate(self):
        new_artwork_path = DEFAULTS["ART_DIR"] / f"{self.name}.py"

        if new_artwork_path.exists():
            raise FileExistsError(f'Artwork already exists: "{new_artwork_path}"')

        with new_artwork_path.open("w") as f:
            print(self.template, file=f)

        print("* written:", new_artwork_path)
