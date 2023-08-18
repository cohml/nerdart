import os
from pathlib import Path
import re

from fastapi import FastAPI
from fastapi.responses import FileResponse


SETUP_PY_PATH = Path(__file__).parents[1] / 'setup.py'
SETUP_PY_TEXT = SETUP_PY_PATH.read_text()
TITLE = re.search(r'NAME = "(.+)"', SETUP_PY_TEXT).group(1)
DESCRIPTION = re.search(r'DESCRIPTION = "(.+)"', SETUP_PY_TEXT).group(1)


app = FastAPI(
    title=TITLE,
    description=DESCRIPTION,
    host='0.0.0.0',
)


@app.get('/')
def show():
    NERDART_PARENT_DIR = os.environ.get('NERDART_PARENT_DIR')
    custom_dir = Path(NERDART_PARENT_DIR) / TITLE / 'img' / 'custom' / 'container'
    img, = custom_dir.glob('*.png')
    return FileResponse(img)
