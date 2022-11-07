import subprocess
import sys

from nerdart import Logo, Template
from nerdart.utils import get_artwork_paths


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
        available_subcommands = ['logo', 'ls', 'template']
        available_subcommands += sorted(artwork_names)
        available_subcommands_msg = (
            '\033[1mThe following subcommands are currently available:\033[0m'
        )
        print(available_subcommands_msg, available_subcommands, sep='\n')

    elif subcommand == 'logo':
        displayed = Logo().display()
        if not displayed:
            print('To see the `nerdart` logo, increase your terminal width.')

    elif subcommand == 'template':
        if len(options) == 0:
            raise ValueError(
                'To initialize a new artwork from a template, supply a name as '
                '`nerdart template <foo>`. This will create the file `foo.py`.'
            )
        name = options[0]
        Template(name).generate()

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
