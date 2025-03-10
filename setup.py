from pathlib import Path
from setuptools import find_packages, setup

__version__ = (Path(__file__) .parent / "VERSION").read_text().strip()

# package metadata
NAME = "nerdart"
VERSION = __version__
DESCRIPTION = "Nerdy art made with math and code."
URL = "https://github.com/cohml/nerdart"
AUTHOR = "cohml"
REQUIRES_PYTHON = ">=3.9.0"
ENTRY_POINTS = ["nerdart = nerdart.utils.run:main"]


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    python_requires=REQUIRES_PYTHON,
    entry_points={"console_scripts": ENTRY_POINTS},
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
)
