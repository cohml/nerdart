import subprocess
import sys

from nerdart.util.logo import Logo
from nerdart.util.utils import get_artwork_paths


def main():
    ls_msg = 'To see which subcommands are available, run `nerdart ls`.'

    if len(sys.argv) == 1:
        raise ValueError(
            '`nerdart` must be followed by exactly one subcommand. ' + ls_msg
        )

    subcommand, *options = sys.argv[1:]
    artwork_paths = get_artwork_paths()
    artwork_names = [ap.stem for ap in artwork_paths]

    if subcommand == 'ls':
        print(
            'The following subcommands are currently available:',
            ['logo', 'ls'] + sorted(artwork_names)
        )

    elif subcommand == 'logo':
        displayed = Logo.display()
        if not displayed:
            print('To see the `nerdart` logo, increase your terminal width.')

    elif subcommand not in artwork_names:
        raise ValueError(
            f'Subcommand not recognized: {subcommand}. ' + ls_msg
        )

    else:
        index = artwork_names.index(subcommand)
        artwork_path = artwork_paths[index]
        subcommand = ['python', artwork_path, *options]
        subprocess.run(subcommand)


if __name__ == '__main__':
    main()
