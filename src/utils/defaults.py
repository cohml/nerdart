from pathlib import Path

DEFAULTS = {
    'IMG_DIR' : Path(__file__).resolve().parent.parent.parent / 'img',
    'IMG_FTYPE' : '.png',
   'SAVEFIG-KWARGS' : {
        'bbox_inches' : 'tight',
        'dpi' : 150,
        'figsize' : (10, 15)
    }
}
