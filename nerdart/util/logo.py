from os import get_terminal_size
from random import shuffle


FORMAT = '\033[1;{color}m{text}\033[0m'

RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
PINK = 35
CYAN = 36
WHITE = 37
WHITE_BLINK = 5
COLORS = [RED, GREEN, YELLOW, BLUE, PINK, CYAN, WHITE]
shuffle(COLORS)

N_TXT = '         _\n        /\\ \\     _\n       /  \\ \\   /\\_\\\n      / /\\ \\ \\_/ / /\n     / / /\\ \\___/ /\n    / / /  \\/____/\n   / / /    / / /\n  / / /    / / /\n / / /    / / /\n/ / /    / / /\n\\/_/     \\/_/'
E_TXT = '             _      \n    /\\ \\ \n /  \\ \\\n/ /\\ \\ \\\n/ / /\\ \\_\\\n/ /_/_ \\/_/\n/ /____/\\ \n/ /\\____\\/ \n/ / /______ \n/ / /_______\\\n \\/__________/'
R_TXT = '      _   \n        /\\ \\ \n       /  \\ \\\n     / /\\ \\ \\ \n   / / /\\ \\_\\\n  / / /_/ / /\n   / / /__\\/ /\n  / / /_____/\n / / /\\ \\ \\  \n/ / /  \\ \\ \\ \n\\/_/    \\_\\/'
D_TXT = '       _        \n      /\\ \\      \n     /  \\ \\____ \n  / /\\ \\_____\\\n / / /\\/___  /\n/ / /   / / /\n/ / /   / / /\n/ / /   / / /\n\\ \\ \\__/ / /\n \\ \\___\\/ /\n   \\/_____/'
A_TXT = '    _             \n   / /\\        \n  / /  \\       \n / / /\\ \\       \n/ / /\\ \\ \\       \n/ / /  \\ \\ \\      \n/ / /___/ /\\ \\   \n/ / /_____/ /\\ \\  \n/ /_________/\\ \\ \\ \n/ / /_       __\\ \\_\\\n \\_\\___\\     /____/_/'
T_TXT = '       _       \n      /\\ \\     \n      \\_\\ \\    \n    /\\__ \\   \n   / /_ \\ \\  \n  / / /\\ \\ \\ \n  / / /  \\/_/ \n  / / /        \n / / /         \n/_/ /          \n \\_\\/'
BOXES_TXT = (' _   ' * 19) + ' _\n' + ('/\\_\\ ' * 19) + '/\\_\\\n' + ('\\/_/ ' * 19) + '\\/_/\n'

N_FMT = {'text' : N_TXT.splitlines(), 'color' : COLORS[0]}
E_FMT = {'text' : E_TXT.splitlines(), 'color' : COLORS[1]}
R_FMT1 = {'text' : R_TXT.splitlines(), 'color' : COLORS[2]}
D_FMT = {'text' : D_TXT.splitlines(), 'color' : COLORS[3]}
A_FMT = {'text' : A_TXT.splitlines(), 'color' : COLORS[4]}
R_FMT2 = {'text' : R_TXT.splitlines(), 'color' : COLORS[5]}
T_FMT = {'text' : T_TXT.splitlines(), 'color' : COLORS[6]}
BOXES_FMT = {'text' : BOXES_TXT, 'color' : WHITE_BLINK}


class Logo:

    def __init__(self):
        boxes_blinking = FORMAT.format(**BOXES_FMT)

        nerdart_colored = ''
        for line in range(len(N_FMT['text'])):
            for letter in (N_FMT, E_FMT, R_FMT1, D_FMT, A_FMT, R_FMT2, T_FMT):
                nerdart_colored += FORMAT.format(
                    color=letter['color'],
                    text=letter['text'][line]
                )
            nerdart_colored += '\n'
        nerdart_colored += '\n'

        self.__logo = (
            boxes_blinking +
            nerdart_colored +
            boxes_blinking
        )

    @property
    def logo(self):
        return self.__logo

    def display(self):
        terminal_width = get_terminal_size().columns
        logo_length = 99
        displayed = False

        if terminal_width >= logo_length:
            displayed = True
            print(self.logo)

        return displayed
