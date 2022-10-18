from pathlib import Path


DEFAULTS = {
    'FIGSIZE' : (15, 10),
    'IMG_DIR' : Path(__file__).resolve().parent.parent / 'img' / 'custom',
    'IMG_SUFFIX' : '.png',
    'SAVEFIG_KWARGS' : {
        'bbox_inches' : 'tight',
        'dpi' : 300
    }
}
