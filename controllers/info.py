import discord
from assets import defaults
import random

from utils.clientWrapper import client
from utils import symbols

validShapes = ','.join([shape for shape in symbols.shapes if shape != 'height'])

client.remove_command('help')

clientAdj = ['rogue', 'stupid', 'loyal', 'pretty', 'gay', 'criminal', 'nut']


@client.command()
async def help(context):
    embed = discord.Embed(title="Bargle client", description="Akhil's " + random.choice(clientAdj) + " client." +
                                                             "\nCommands are the following: \n",
                          color=defaults.CLIENT_COLOR)

    embed.add_field(name=defaults.COMMAND_PREFIX + "draw [phrase] [fill,] [space,]",
                    value="Draws **phrase** as the combination of **fill** and **space**. " +
                          "\n**fill** text that draws the word, accepts multiple args delimited by commas"
                          "\n**space** fills the space between fill, accepts multiple args delimited by commas" +
                          "\nTry ~draw meme :thinking:,:heart: :flag_in:,:ok_hand:",
                    inline=False)

    embed.add_field(name=defaults.COMMAND_PREFIX + "drawline [phrase] [fill,] [space,]",
                    value="Same as **draw** but displays letters horizontally.",
                    inline=False)

    embed.add_field(name=defaults.COMMAND_PREFIX + "drawshape [shape] [fill,] [space,]",
                    value="Draws shapes!\n" +
                          "Valid shapes are [" + validShapes + "]",
                    inline=False)

    embed.add_field(name=defaults.COMMAND_PREFIX + "hi",
                    value="Friendly greetings!",
                    inline=False)

    embed.add_field(name=defaults.COMMAND_PREFIX + "emoji",
                    value=":(",
                    inline=False)

    embed.add_field(name=defaults.COMMAND_PREFIX + "food",
                    value="Serves delicious **free** food",
                    inline=False)

    embed.add_field(name=defaults.COMMAND_PREFIX + "menu",
                    value="Menu for " + context.guild.name + ". Careful, changes very quickly!",
                    inline=False)

    embed.add_field(name=defaults.COMMAND_PREFIX + "claimwaifu [member]",
                    value="Claim another fellow guild member as your waifu. I don't get this sick shit.",
                    inline=False)

    embed.add_field(name=defaults.COMMAND_PREFIX + "waifus",
                    value="List of guild waifus. ~kyaaa",
                    inline=False)

    embed.add_field(name=defaults.COMMAND_PREFIX + "info",
                    value="General client information.",
                    inline=False)

    await context.send(embed=embed)


@client.command()
async def info(context):
    creator = client.get_user(90508678297313280)

    embed = discord.Embed(title="Bargle client", description="Akhil's " + random.choice(clientAdj) + " client.",
                          color=defaults.CLIENT_COLOR)
    embed.add_field(name="Author", value=creator.name)
    embed.add_field(name="Server count", value=f"{len(client.guilds)}")
    embed.add_field(name="Invite",
                    value="[Bargle client](https://discordapp.com/api/oauth2/authorize?client_id=221714409574236160&permissions=329792&scope=client)")

    await context.send(embed=embed)
