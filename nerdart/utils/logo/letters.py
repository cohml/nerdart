from .colors import COLORS

N_TEXT = "         _\n        /\\ \\     _\n       /  \\ \\   /\\_\\\n      / /\\ \\ \\_/ / /\n     / / /\\ \\___/ /\n    / / /  \\/____/\n   / / /    / / /\n  / / /    / / /\n / / /    / / /\n/ / /    / / /\n\\/_/     \\/_/"
E_TEXT = "             _      \n    /\\ \\ \n /  \\ \\\n/ /\\ \\ \\\n/ / /\\ \\_\\\n/ /_/_ \\/_/\n/ /____/\\ \n/ /\\____\\/ \n/ / /______ \n/ / /_______\\\n \\/__________/"
R_TEXT = "      _   \n        /\\ \\ \n       /  \\ \\\n     / /\\ \\ \\ \n   / / /\\ \\_\\\n  / / /_/ / /\n   / / /__\\/ /\n  / / /_____/\n / / /\\ \\ \\  \n/ / /  \\ \\ \\ \n\\/_/    \\_\\/"
D_TEXT = "       _        \n      /\\ \\      \n     /  \\ \\____ \n  / /\\ \\_____\\\n / / /\\/___  /\n/ / /   / / /\n/ / /   / / /\n/ / /   / / /\n\\ \\ \\__/ / /\n \\ \\___\\/ /\n   \\/_____/"
A_TEXT = "    _             \n   / /\\        \n  / /  \\       \n / / /\\ \\       \n/ / /\\ \\ \\       \n/ / /  \\ \\ \\      \n/ / /___/ /\\ \\   \n/ / /_____/ /\\ \\  \n/ /_________/\\ \\ \\ \n/ / /_       __\\ \\_\\\n \\_\\___\\     /____/_/"
T_TEXT = "       _       \n      /\\ \\     \n      \\_\\ \\    \n    /\\__ \\   \n   / /_ \\ \\  \n  / / /\\ \\ \\ \n  / / /  \\/_/ \n  / / /        \n / / /         \n/_/ /          \n \\_\\/"

N = {"text": N_TEXT.splitlines(), "color": COLORS[0]}
E = {"text": E_TEXT.splitlines(), "color": COLORS[1]}
R1 = {"text": R_TEXT.splitlines(), "color": COLORS[2]}
D = {"text": D_TEXT.splitlines(), "color": COLORS[3]}
A = {"text": A_TEXT.splitlines(), "color": COLORS[4]}
R2 = {"text": R_TEXT.splitlines(), "color": COLORS[5]}
T = {"text": T_TEXT.splitlines(), "color": COLORS[6]}

LETTERS = [N, E, R1, D, A, R2, T]
