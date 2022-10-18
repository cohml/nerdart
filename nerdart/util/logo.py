from os import get_terminal_size


_RESET = '\033[0m'
_BLINK = '\033[1;5m{}' + _RESET
_RED = '\033[1;31m' + '{}' + _RESET
_GREEN = '\033[1;32m' + '{}' + _RESET
_YELLOW = '\033[1;33m' + '{}' + _RESET
_BLUE = '\033[1;34m' + '{}' + _RESET
_PINK = '\033[1;35m' + '{}' + _RESET
_CYAN = '\033[1;36m' + '{}' + _RESET
_WHITE = '\033[1;37m' + '{}' + _RESET
_BOXES = r""" _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _    _
/\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\ /\_\
\/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/ \/_/"""
_N = '         _\n        /\\ \\     _\n       /  \\ \\   /\\_\\\n      / /\\ \\ \\_/ / /\n     / / /\\ \\___/ /\n    / / /  \\/____/\n   / / /    / / /\n  / / /    / / /\n / / /    / / /\n/ / /    / / /\n\\/_/     \\/_/'
_E = '             _      \n    /\\ \\ \n /  \\ \\\n/ /\\ \\ \\\n/ / /\\ \\_\\\n/ /_/_ \\/_/\n/ /____/\\ \n/ /\\____\\/ \n/ / /______ \n/ / /_______\\\n \\/__________/'
_R = '      _   \n        /\\ \\ \n       /  \\ \\\n     / /\\ \\ \\ \n   / / /\\ \\_\\\n  / / /_/ / /\n   / / /__\\/ /\n  / / /_____/\n / / /\\ \\ \\  \n/ / /  \\ \\ \\ \n\\/_/    \\_\\/'
_D = '       _        \n      /\\ \\      \n     /  \\ \\____ \n  / /\\ \\_____\\\n / / /\\/___  /\n/ / /   / / /\n/ / /   / / /\n/ / /   / / /\n\\ \\ \\__/ / /\n \\ \\___\\/ /\n   \\/_____/'
_A = '    _             \n   / /\\        \n  / /  \\       \n / / /\\ \\       \n/ / /\\ \\ \\       \n/ / /  \\ \\ \\      \n/ / /___/ /\\ \\   \n/ / /_____/ /\\ \\  \n/ /_________/\\ \\ \\ \n/ / /_       __\\ \\_\\\n \\_\\___\\     /____/_/'
_T = '       _       \n      /\\ \\     \n      \\_\\ \\    \n    /\\__ \\   \n   / /_ \\ \\  \n  / / /\\ \\ \\ \n  / / /  \\/_/ \n  / / /        \n / / /         \n/_/ /          \n \\_\\/'


class Logo:

    _letters = [_N, _E, _R, _D, _A, _T]
    _nerdart = '\n'.join(
        [
            _RED.format(n) +
            _GREEN.format(e) +
            _YELLOW.format(r) +
            _BLUE.format(d) +
            _PINK.format(a) +
            _CYAN.format(r) +
            _WHITE.format(t)
            for n, e, r, d, a, t in zip(*map(str.splitlines, _letters))
        ]
    )
    _logo = '\n'.join(
        [
            _BLINK.format(_BOXES),
            _nerdart,
            _BLINK.format(_BOXES),
            ''
        ]
    )


    @classmethod
    def display(cls):
        terminal_width = get_terminal_size().columns
        logo_length = 99
        displayed = False

        if terminal_width >= logo_length:
            print(cls._logo)
            displayed = True

        return displayed
