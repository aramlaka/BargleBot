import random


class MemeGen:

    def __init__(self, alphabet):
        self.alphabet = alphabet

    def symbols(self, phrase):
        return [self.alphabet.get(x) for x in phrase.lower()]

    def lines(self, symbols):
        lines = ['' for x in range(self.alphabet.get('height'))]

        for symbol in symbols:
            for i, line in enumerate(symbol.split("\n")):
                lines[i] += line

        return lines

    def create(self, phrase, fill, space, style='partition', choice='alternate'):
        symbols = self.symbols(phrase)

        fill = fill.split(',')
        space = space.split(',')

        for i, symbol in enumerate(symbols):

            if choice is 'alternate':
                symbols[i] = symbol.replace('+', fill[i % len(fill)]).\
                    replace('-', space[i % len(space)])
            elif choice is 'random':
                symbols[i] = symbol.replace('+', random.choice(fill))\
                    .replace('-', random.choice(space))

        if style is 'lines':
            return self.lines(symbols)
        elif style is 'whole':
            return '\n'.join(self.lines(symbols))

        return symbols


def meme_print(meme):
    for line in meme:
        print(line)
