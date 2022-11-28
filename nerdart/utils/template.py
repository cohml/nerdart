from nerdart import DEFAULTS

ART_DIR = DEFAULTS["ART_DIR"]
TEMPLATE_RAW = """

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
    @staticmethod
    def generate(name):
        new_artwork_path = ART_DIR / (name + ".py")

        if new_artwork_path.exists():
            raise FileExistsError(f'Artwork already exists: "{new_artwork_path}"')

        with new_artwork_path.open("w") as f:
            print(TEMPLATE_RAW.strip(), file=f)

        print("* written:", new_artwork_path)

    @staticmethod
    def throw():
        raise ValueError(
            "To initialize a new artwork `foo` using a template, supply a "
            "name as `nerdart template foo`. This will create the file "
            f'"{ART_DIR}/foo.py".'
        )
