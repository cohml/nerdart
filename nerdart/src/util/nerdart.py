import subprocess
import sys

from nerdart.src.util.utils import get_script_paths, print_logo


def main():
    ls_msg = 'To see which subcommands are available, run `nerdart ls`.'

    if len(sys.argv) == 1:
        raise ValueError(
            '`nerdart` must be followed by exactly one subcommand. ' + ls_msg
        )

    entry_point, *options = sys.argv[1:]
    full_paths = get_script_paths()
    entry_points = [p.stem for p in full_paths]

    if entry_point == 'ls':
        print(
            'The following subcommands are currently available:',
            ['logo', 'ls'] + sorted(entry_points)
        )

    elif entry_point == 'logo':
        printed = print_logo()
        if not printed:
            print('To see the `nerdart` logo, increase your terminal width.')

    elif entry_point not in entry_points:
        raise ValueError(
            f'Subcommand not recognized: {entry_point}. ' + ls_msg
        )

    else:
        i = entry_points.index(entry_point)
        path_to_script = full_paths[i]
        subcommand = ['python', path_to_script, *options]
        subprocess.run(subcommand)


if __name__ == '__main__':
    main()
