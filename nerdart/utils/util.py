import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from time import perf_counter

from nerdart.utils.defaults import DEFAULTS
from nerdart.utils.logo.logo import Logo


def get_artwork_paths():
    art_dir = Path(__file__).resolve().parent.parent / 'art'
    relative_paths = art_dir.glob('*.py')
    absolute_paths = [
         rp.resolve() for rp in relative_paths if rp.name != '__init__.py'
    ]
    return absolute_paths


def save_or_show(file_dunder):

    def decorator(artwork_func):
        Logo().display()

        def wrapper(cli_args):
            start = perf_counter()
            artwork_func(cli_args)
            end = perf_counter()

            # compute and display duration to generate art
            duration = end - start
            minutes = int(np.round(duration // 60, 0))
            seconds = int(np.round(duration % 60, 0))
            print(f'* artwork generated in {minutes}m {seconds}s')

            # show image in popup window if `--save` not passed; don't save to file
            if cli_args.save is None:
                plt.tight_layout()

            else:
                skip = {'save', 'suffix'}
                params = ','.join(f'{k}={v}' for k, v in vars(cli_args).items()
                                             if k not in skip)

                # set filepath to value passed under `--save`
                if cli_args.save:
                    save_path = cli_args.save
                # set filepath to default value if `--save` passed without argument
                else:
                    DEFAULTS['IMG_DIR'].mkdir(exist_ok=True, parents=True)
                    save_basename = f'{Path(file_dunder).stem},{params}{cli_args.suffix}'
                    save_path = DEFAULTS['IMG_DIR'] / save_basename

                plt.gcf().set_size_inches(DEFAULTS['FIGSIZE'])
                plt.savefig(save_path, **DEFAULTS['SAVEFIG_KWARGS'])
                print('* written:', save_path)

            if not cli_args.quiet:
                plt.show()

        return wrapper
    return decorator


def xy(arr):
    x = np.sin(arr)
    y = np.cos(arr)
    return x, y
