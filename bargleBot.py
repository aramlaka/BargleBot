import discord
import symbols

from memeText import MemeGen
import discord_token
from discord.ext import commands


bot = commands.Bot(command_prefix='~', description="Akhil's loyal bargle bot.")
bot.remove_command('help')
mText = MemeGen(symbols.english_alphabet)
mShapes = MemeGen(symbols.shapes)


@bot.event
async def on_ready():
    print('Login successful')
    print('User: ', bot.user.name)
    print('ID: ', bot.user.id)


@bot.command()
async def draw(ctx, phrase: str, fill: str, space: str):
    meme = mText.create(phrase, fill, space)
    for line in meme:
        await ctx.send(line)

@bot.command()
async def drawline(ctx, phrase: str, fill: str, space: str):
    meme = mText.create(phrase, fill, space, style='lines')
    for line in meme:
        await ctx.send(line)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Bargle Bot", description="Akhil's loyal bargle bot. Commands are the following: ",
                          color=0xeee657)

    embed.add_field(name="~draw phrase [fill,] [space,]",
                    value="Draws **phrase** as the combination of **fill** and **space**. " +
                          "\n**fill** and **space** accept multiple inputs separated by commas" +
                          "\nTry ~draw meme :thinking:,:heart: :flag_in:,:ok_hand:",
                    inline=False)

    await ctx.send(embed=embed)

bot.run(discord_token.current_token)
