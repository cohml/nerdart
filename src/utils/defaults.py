from pathlib import Path

DEFAULTS = {
    'IMG_DIR' : Path(__file__).resolve().parent.parent.parent / 'img',
    'SAVE' : {
        'bbox_inches' : 'tight',
        'dpi' : 150,
        'figsize' : (10, 15)
    }
}
