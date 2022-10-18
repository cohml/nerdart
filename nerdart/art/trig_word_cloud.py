import numpy as np
import matplotlib.pyplot as plt

from itertools import cycle
from pathlib import Path

from nerdart.util.parser import Parser
from nerdart.util.utils import save_or_show


@save_or_show(__file__)
def plot(args):
    path_to_word_file = args.path_to_word_file
    n_words_per_line = args.n_words_per_line
    n_lines = args.n_lines
    fontsize = args.fontsize
    rotate = args.rotate
    dizziness = args.dizziness
    unique = args.unique
    ordered = args.ordered

    words = path_to_word_file.read_text().lower().splitlines()
    if unique:
        words = sorted(set(words), key=words.index)

    inverse_word_lengths = np.array([1 / len(word) for word in words])
    sampling_probabilities = inverse_word_lengths / inverse_word_lengths.sum()
    rotations = cycle(np.linspace(-np.pi, np.pi, n_words_per_line) * dizziness)

    ax = plt.subplot()
    x = np.linspace(-np.pi, np.pi, n_words_per_line)
    y = np.sin(x)
    c = plt.cm.rainbow(np.linspace(0, 1, x.size))

    for i in range(n_lines):
        ci = cycle(c)
        for _ in range(round(i * (x.size / n_lines))):
            next(ci)
        for j, (xj, yj, cj) in enumerate(zip(x, y, ci), start=1):
            if ordered:
                word = words[i * j]
            else:
                word = np.random.choice(words, p=sampling_probabilities)

            xy = (xj, yj + i)
            s = fontsize * (1 - abs(yj)) + fontsize
            r = next(rotations)
            ax.annotate(word,
                        xy,
                        c=cj,
                        ha='center',
                        va='center',
                        weight='ultralight',
                        fontsize=s,
                        rotation=r if rotate else 0)

    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(-1, i + 1)
    ax.axis('off')


def main():
    parser = Parser()
    parser.add('-p', '--path_to_word_file',
               type=Path,
               default='/usr/share/dict/words',
               help='must be a plaintext file with one word per line')
    parser.add('-w', '--n_words_per_line', type=int, default=50)
    parser.add('-l', '--n_lines', type=int, default=5)
    parser.add('-f', '--fontsize', type=int, default=10)
    parser.add('-r', '--rotate', action='store_true')
    parser.add('-d', '--dizziness',
               type=float,
               default=50.0,
               help='use with `rotate`')
    parser.add('-u', '--unique', action='store_true')
    parser.add('-o', '--ordered',
               action='store_true',
               help='show words in order of entry in word file; '
                    'if not passed, randomly sample words weighted '
                    'inversely by length')
    args = parser.parse()
    plot(args)


if __name__ == '__main__':
    main()
