import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from util.defaults import DEFAULTS


def save_or_show(file_dunder):

    def decorator(plot_func):

        def wrapper(cli_args):
            plot_func(cli_args)

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
                    save_basename = f'{Path(file_dunder).stem},{params}{cli_args.suffix}'
                    save_path = DEFAULTS['IMG_DIR'] / save_basename

                plt.savefig(save_path, **DEFAULTS['SAVEFIG_KWARGS'])
                print('written:', save_path)

            plt.show()

        return wrapper
    return decorator


def xy(arr):
    x = np.sin(arr)
    y = np.cos(arr)
    return x, y
