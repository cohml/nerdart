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


LOGO = (
r""" _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _
/\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\
\/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/
         _             _            _          _            _                   _         _
        /\ \     _    /\ \         /\ \       /\ \         / /\                /\ \      /\ \
       /  \ \   /\_\ /  \ \       /  \ \     /  \ \____   / /  \              /  \ \     \_\ \
      / /\ \ \_/ / // /\ \ \     / /\ \ \   / /\ \_____\ / / /\ \            / /\ \ \    /\__ \
     / / /\ \___/ // / /\ \_\   / / /\ \_\ / / /\/___  // / /\ \ \          / / /\ \_\  / /_ \ \
    / / /  \/____// /_/_ \/_/  / / /_/ / // / /   / / // / /  \ \ \        / / /_/ / / / / /\ \ \
   / / /    / / // /____/\    / / /__\/ // / /   / / // / /___/ /\ \      / / /__\/ / / / /  \/_/
  / / /    / / // /\____\/   / / /_____// / /   / / // / /_____/ /\ \    / / /_____/ / / /
 / / /    / / // / /______  / / /\ \ \  \ \ \__/ / // /_________/\ \ \  / / /\ \ \  / / /
/ / /    / / // / /_______\/ / /  \ \ \  \ \___\/ // / /_       __\ \_\/ / /  \ \ \/_/ /
\/_/     \/_/ \/__________/\/_/    \_\/   \/_____/ \_\___\     /____/_/\/_/    \_\/\_\/
 _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _
/\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\
\/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/
"""
)
