import matplotlib.pyplot as plt
import numpy as np

from itertools import cycle
from pathlib import Path

## params
words_per_line = 50
lines = 5
fontsize = 10
rotate = False

word_file = '/usr/share/dict/words'
words = list(set(Path(word_file).read_text().lower().splitlines()))
lens = [1 / len(word) for word in words]
sum_ = sum(lens)
probs = np.array([l / sum_ for l in lens])
rotations = cycle(np.linspace(0, 365, words_per_line))

ax = plt.subplot()
x = np.linspace(-np.pi, np.pi, words_per_line)
y = np.sin(x)
c = plt.cm.rainbow(np.linspace(0, 1, x.size))

for i in range(lines):
    ci = cycle(c)
    for _ in range(round(i * (x.size / lines))):
        next(ci)
    for xj, yj, cj in zip(x, y, ci):
        word = np.random.choice(words, p=probs)
        xy = (xj, yj + i)
        size = fontsize * (1 - abs(yj)) + fontsize
        r = next(rotations)
        ax.annotate(word,
                    xy,
                    c=cj,
                    ha='center',
                    va='center',
                    weight='ultralight',
                    fontsize=size,
                    rotation=r if rotate else 0)

ax.set_xlim(x.min(), x.max())
ax.set_ylim(-1, i + 1)
ax.axis('off')

plt.show()
