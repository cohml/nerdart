from pathlib import Path
__version__ = (Path(__file__).parents[1] / "VERSION").read_text().strip()

from nerdart.utils.defaults import DEFAULTS
from nerdart.utils.logo.logo import Logo
from nerdart.utils.parser import Parser
from nerdart.utils.template import Template
