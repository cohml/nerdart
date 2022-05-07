import argparse
from .defaults import DEFAULTS


class Parser:

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description=f'{" Go make some art, nerd !!! ":*^100}',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
        self.parser.add_argument(
            '-S', '--save',
            nargs='?',
            help='Pass to save image, else image will only be displayed via a '
                 'popup window. If passing a filepath, that will be used to '
                 'save the image, otherwise the following path will be used: '
                 f'{DEFAULTS["IMG_DIR"]}/<script_basename>.png'
        )
        self.parser.add_argument(
            '-X', '--suffix',
            default=DEFAULTS['IMG_SUFFIX'],
            help='Filetype extension to use when saving images (default: '
                 '%(default)s)'
        )

    def add(self, *args, **kwargs):
        kwargs['help'] = kwargs.get('help', ' ') # will show defaults if no help supplied
        self.parser.add_argument(*args, **kwargs)

    def parse(self):
        return self.parser.parse_args()
