import argparse
from .defaults import DEFAULTS


class Parser:

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description=f'{" Go make some art, nerd !!! ":*^100}'
        )
        self.parser.add_argument(
            '-S', '--save_image',
            nargs='*',
            help='Pass to save image, else image will only be displayed via a '
                 'popup window. If passing a filepath, that will be used to '
                 'save the image, otherwise the following path will be used: '
                 f'{DEFAULTS["IMG_DIR"]}/<script_basename>.png'
        )
        self.parser.add_argument(
            '-E', '--filetype_extension',
            default=DEFAULTS['IMG_FTYPE'],
            help='Filetype extension to use when saving images.'
        )

    def add(self, *args, **kwargs):
        self.parser.add_argument(*args, **kwargs)

    def parse(self):
        return self.parser.parse_args()
