from pathlib import Path

DEFAULTS = {
    'IMG_DIR' : Path(__file__).resolve().parent.parent.parent / 'img',
    'IMG_SUFFIX' : '.png',
    'SAVEFIG_KWARGS' : {
        'bbox_inches' : 'tight',
        'dpi' : 300,
        'figsize' : (10, 15)
    }
}
