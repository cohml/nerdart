from shutil import get_terminal_size

from nerdart.utils.defaults import DEFAULTS
from nerdart.utils.logo.boxes import BOXES
from nerdart.utils.logo.letters import LETTERS


FORMAT = DEFAULTS['LOGO_FORMAT']


class Logo:

    def __init__(self):
        boxes_lines = BOXES['text'].splitlines()
        self.max_length = len(boxes_lines[-1])
        self.n_letter_lines = len(LETTERS[-1]['text'])

        blinking_boxes = FORMAT.format(**BOXES)

        colored_letters = ''
        for line in range(self.n_letter_lines):
            for letter in LETTERS:
                colored_letters += FORMAT.format(
                    text=letter['text'][line],
                    color=letter['color']
                )
            colored_letters += '\n'
        colored_letters += '\n'

        self.__logo = (
            blinking_boxes +
            colored_letters +
            blinking_boxes
        )

    @property
    def logo(self):
        return self.__logo

    @property
    def max_length(self):
        return self.__max_length

    @max_length.setter
    def max_length(self, max_length):
        self.__max_length = max_length

    @property
    def n_letter_lines(self):
        return self.__n_letter_lines

    @n_letter_lines.setter
    def n_letter_lines(self, n_letter_lines):
        self.__n_letter_lines = n_letter_lines

    def display(self):
        terminal_width = get_terminal_size().columns
        displayed = False

        if terminal_width >= self.max_length:
            displayed = True
            print(self.logo)

        return displayed
