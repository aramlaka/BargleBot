from memeText import MemeGen
import symbols

a = MemeGen(symbols.english_alphabet)

print("Symbols for 'hi': ", a.symbols("hi"))
print("Lines for 'hi': ", a.lines(a.symbols("hi")))
print("Meme default 'hi': ", a.create("hi", "x", "o"))
print("Meme random 'hi': ", a.create("hi", "x,y,z", "o,m", choice='random'))
print("Meme lines 'hi': ", a.create("hi", "x", "o", style='lines'))
print("Meme random lines 'hi': ", a.create("hi", "x,y,z", "o,m", style='lines', choice='random'))
print("Meme whole 'hi':\n", a.create("hi", "x", "o", style='whole'))
