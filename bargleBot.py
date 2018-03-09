import discord
import symbols
import random

from memeText import MemeGen
import discord_token
from discord.ext import commands

BOT_COLOR = 0x1464e5
COMMAND_PREFIX = '~'
botAdj = ['rogue', 'stupid', 'loyal', 'pretty', 'gay', 'criminal', 'nut']

bot = commands.Bot(command_prefix=COMMAND_PREFIX, description="Akhil's loyal bargle bot.")
bot.remove_command('help')
mText = MemeGen(symbols.english_alphabet)
mShapes = MemeGen(symbols.shapes)


@bot.event
async def on_ready():
    print('Login successful')
    print('User: ', bot.user.name)
    print('ID: ', bot.user.id)


@bot.command()
async def draw(message, phrase: str, fill: str, space: str):
    meme = mText.create(phrase.lower(), fill, space)
    for line in meme:
        await message.send(line)


@bot.command()
async def drawline(message, phrase: str, fill: str, space: str):
    meme = mText.create(phrase.lower(), fill, space, style='lines')
    for line in meme:
        await message.send(line)


@bot.command()
async def drawshape(message, shape: str, fill: str, space: str):
    if shape not in symbols.shapes:
        response = "Invalid shape.\n" \
                   "Valid shapes are: ["

        for shape in symbols.shapes:
            if shape is not 'height':
                response += shape + ","

        response += "]"

        await message.send(response)
    else:
        meme = mShapes.create(shape.lower(), fill, space, shape=True, style='lines')
        for line in meme:
            await message.send(line)


@bot.command()
async def rekt(message):
    await message.send(":gun:")


@bot.command()
async def meme(message):
    embed = discord.Embed(title='meme', color=BOT_COLOR)
    embed.set_image(url='https://cdn.discordapp.com/attachments/109762039823532032/421768416219889674/image.jpg')
    await message.send(embed=embed)


@bot.command()
async def hi(message):
    shitList = ['freddie', 'pupper', 'akhil', 'lily', 'ahri']

    if any(name in message.author.name.lower() for name in shitList):
        response = "fuck off " + message.author.name
    else:
        response = "Hi " + message.author.name + "!"

    await message.send(response)


@bot.command()
async def emoji(message):
    await message.send("i don't have nitro :(")


@bot.command()
async def help(message):
    validShapes = ','.join([shape for shape in symbols.shapes if shape is not 'height'])

    embed = discord.Embed(title="Bargle Bot", description="Akhil's " + random.choice(botAdj) + " bot." +
                                                          "\nCommands are the following: \n",
                          color=BOT_COLOR)

    embed.add_field(name=COMMAND_PREFIX + "draw phrase [fill,] [space,]",
                    value="Draws **phrase** as the combination of **fill** and **space**. " +
                          "\n**fill** text that draws the word, accepts multiple args delimited by commas"
                          "\n**space** fills the space between fill, accepts multiple args delimited by commas" +
                          "\nTry ~draw meme :thinking:,:heart: :flag_in:,:ok_hand:",
                    inline=False)

    embed.add_field(name=COMMAND_PREFIX + "drawline phrase [fill,] [space,]",
                    value="Same as **draw** but displays letters horizontally.",
                    inline=False)

    embed.add_field(name=COMMAND_PREFIX + "drawshape shape [fill,] [space,]",
                    value="Draws shapes!\n" +
                          "Valid shapes are [" + validShapes + "]",
                    inline=False)

    embed.add_field(name=COMMAND_PREFIX + "hi",
                    value="Friendly greetings!",
                    inline=False)

    embed.add_field(name=COMMAND_PREFIX + "emoji",
                    value=":(",
                    inline=False)

    embed.add_field(name=COMMAND_PREFIX + "info",
                    value="General bot information.",
                    inline=False)

    await message.send(embed=embed)


@bot.command()
async def info(message):
    creator = bot.get_user(90508678297313280)

    embed = discord.Embed(title="Bargle Bot", description="Akhil's " + random.choice(botAdj) + " bot.",
                          color=BOT_COLOR)
    embed.add_field(name="Author", value=creator.name)
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    embed.add_field(name="Invite",
                    value="[Bargle Bot](https://discordapp.com/api/oauth2/authorize?client_id=221714409574236160&permissions=329792&scope=bot)")

    await message.send(embed=embed)

bot.run(discord_token.current_token)
