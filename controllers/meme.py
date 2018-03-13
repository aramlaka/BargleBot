import discord
from assets import defaults

from utils import symbols, memeText
from utils.clientWrapper import client

botAdj = ['rogue', 'stupid', 'loyal', 'pretty', 'gay', 'criminal', 'nut']
shitList = ['freddie', 'pupper', 'akhil', 'lily', 'ahri']
validShapes = ','.join([shape for shape in symbols.shapes if shape != 'height'])

mText = memeText.MemeGen(symbols.english_alphabet)
mShapes = memeText.MemeGen(symbols.shapes)


@client.command()
async def draw(context, phrase: str, fill: str, space: str):
    meme = mText.create(phrase.lower(), fill, space)
    for line in meme:
        await context.send(line)


@client.command()
async def drawline(context, phrase: str, fill: str, space: str):
    meme = mText.create(phrase.lower(), fill, space, style='lines')
    for line in meme:
        await context.send(line)


@client.command()
async def drawshape(context, shape: str, fill: str, space: str):
    if shape not in symbols.shapes:
        response = "Invalid shape.\n" \
                   "Valid shapes are: [" + validShapes + "]"
        await context.send(response)
    else:
        meme = mShapes.create(shape.lower(), fill, space, shape=True, style='lines')
        for line in meme:
            await context.send(line)


@client.command()
async def rekt(context):
    await context.send(":gun:")


@client.command()
async def meme(context):
    embed = discord.Embed(title='meme', color=defaults.CLIENT_COLOR)
    embed.set_image(url='https://cdn.discordapp.com/attachments/109762039823532032/421768416219889674/image.jpg')
    await context.send(embed=embed)


@client.command()
async def hi(context):
    if any(name in context.author.name.lower() for name in shitList):
        response = "fuck off " + context.author.name
    else:
        response = "Hi " + context.author.name + "!"

    await context.send(response)


@client.command()
async def emoji(context):
    await context.send("i don't have nitro :(")


