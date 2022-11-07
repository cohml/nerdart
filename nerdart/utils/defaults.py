from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parent.parent

DEFAULTS = {
    'ART_DIR' : PACKAGE_ROOT / 'art',
    'FIGSIZE' : (15, 10),
    'IMG_DIR' : PACKAGE_ROOT / 'img' / 'custom',
    'IMG_SUFFIX' : '.png',
    'LOGO_FORMAT' : '\033[1;{color}m{text}\033[0m',
    'SAVEFIG_KWARGS' : {
        'bbox_inches' : 'tight',
        'dpi' : 300
    }
}
