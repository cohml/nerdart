import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from util.defaults import DEFAULTS


def save_or_show(args, file):

    if args.save is None:
        plt.show()

    else:
        skip = ['save', 'suffix']
        params = ','.join(f'{k}={v}' for k, v in vars(args).items() if k not in skip)

        if args.save:
            save_path, = args.save
        else:
            save_path = DEFAULTS['IMG_DIR'] / f'{Path(file).stem}_{params}{args.suffix}'

        plt.savefig(save_path, **DEFAULTS['SAVEFIG_KWARGS'])
        print('written:', save_path)


def xy(arr):
    x = np.sin(arr)
    y = np.cos(arr)
    return x, y
