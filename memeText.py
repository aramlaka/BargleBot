import random


class MemeGen:

    def __init__(self, alphabet):
        self.alphabet = alphabet

    def symbols(self, phrase):
        return [self.alphabet.get(x) for x in phrase]

    def lines(self, symbols, space, padding=1):
        lines = ['' for x in range(self.alphabet.get('height'))]

        for symbol in symbols:
            for i, line in enumerate(symbol.split("\n")):
                pad = padding * space[i % len(space)]
                lines[i] += pad + line + pad

        return lines

    def create(self, phrase, fill, space, style='partition', choice='alternate', shape=False):
        if shape:
            phrase = phrase.split(',')

        symbols = self.symbols(phrase)

        fill = fill.split(',')
        space = space.split(',')

        if choice is 'random':
            fill = random.shuffle(choice)
            space = space.shuffle(choice)

        for i, symbol in enumerate(symbols):
            symbols[i] = symbol.replace('+', fill[i % len(fill)]).\
                replace('-', space[i % len(space)])

        if style is 'lines':
            return self.lines(symbols, space)
        elif style is 'whole':
            return '\n'.join(self.lines(symbols, space))

        return symbols


def meme_print(meme):
    for line in meme:
        print(line)
