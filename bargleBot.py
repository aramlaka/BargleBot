import discord
import symbols
import random

from memeText import MemeGen
import discord_token
from discord.ext import commands

BOT_COLOR = 0x1464e5
COMMAND_PREFIX = '~'
botAdj = ['rogue', 'stupid', 'loyal', 'pretty', 'gay', 'criminal', 'nut']
shitList = ['freddie', 'pupper', 'akhil', 'lily', 'ahri']
validShapes = ','.join([shape for shape in symbols.shapes if shape != 'height'])
foodItems = [':green_apple:', ':apple:', ':pear:', ':tangerine:', ':tangerine:', ':lemon:', ':banana:', ':watermelon:',
             ':grapes:', ':strawberry:', ':melon:', ':cherries:', ':peach:', ':pineapple:', ':tomato:', ':eggplant:',
             ':hot_pepper:', ':corn:', ':sweet_potato:', ':honey_pot:', ':bread:', ':cheese:', ':poultry_leg:',
             ':meat_on_bone:', ':fried_shrimp:', ':cooking:', ':hamburger:', ':fries:', ':hotdog:', ':pizza:',
             ':spaghetti:',
             ':taco:', ':burrito:', ':ramen:', ':stew:', ':fish_cake:', ':sushi:', ':bento:', ':curry:', ':rice_ball:',
             ':rice:', ':rice_cracker:', ':oden:', ':dango:', ':shaved_ice:', ':ice_cream:', ':icecream:', ':cake:',
             ':birthday:', ':custard:', ':candy:', ':lollipop:', ':chocolate_bar:', ':popcorn:', ':doughnut:',
             ':cookie:',
             ':beer:', ':beers:', ':wine_glass:', ':cocktail:', ':tropical_drink:', ':champagne:', ':sake:', ':tea:',
             ':coffee:', ':baby_bottle:', ':croissant:', ':avocado:', ':cucumber:', ':bacon:', ':potato:', ':carrot:',
             ':french_bread:', ':salad:', ':shallow_pan_of_food:', ':stuffed_flatbread:', ':tumbler_glass:', ':egg:',
             ':milk:', ':peanuts:', ':kiwi:', ':pancakes:']
claims = {}

bot = commands.Bot(command_prefix=COMMAND_PREFIX, description="Akhil's loyal bargle bot.")
bot.remove_command('help')
mText = MemeGen(symbols.english_alphabet)
mShapes = MemeGen(symbols.shapes)


@bot.event
async def on_ready():
    print('Login successful')
    print('User: ', bot.user.name)
    print('ID: ', bot.user.id)


# @bot.event
# async def on_context(context):
#    if any(emoji in context.content for emoji in ['👖']):
#        channel = context.channel
#        embed = discord.Embed(title='🦆👖', color=BOT_COLOR)
#        embed.add_field(name='ohno', value='https://www.youtube.com/watch?v=1PaKYvMdH3o')
#        await channel.send(embed=embed)


@bot.command()
async def draw(context, phrase: str, fill: str, space: str):
    meme = mText.create(phrase.lower(), fill, space)
    for line in meme:
        await context.send(line)


@bot.command()
async def drawline(context, phrase: str, fill: str, space: str):
    meme = mText.create(phrase.lower(), fill, space, style='lines')
    for line in meme:
        await context.send(line)


@bot.command()
async def drawshape(context, shape: str, fill: str, space: str):
    if shape not in symbols.shapes:
        response = "Invalid shape.\n" \
                   "Valid shapes are: [" + validShapes + "]"
        await context.send(response)
    else:
        meme = mShapes.create(shape.lower(), fill, space, shape=True, style='lines')
        for line in meme:
            await context.send(line)


@bot.command()
async def rekt(context):
    await context.send(":gun:")


@bot.command()
async def meme(context):
    embed = discord.Embed(title='meme', color=BOT_COLOR)
    embed.set_image(url='https://cdn.discordapp.com/attachments/109762039823532032/421768416219889674/image.jpg')
    await context.send(embed=embed)


@bot.command()
async def hi(context):
    if any(name in context.author.name.lower() for name in shitList):
        response = "fuck off " + context.author.name
    else:
        response = "Hi " + context.author.name + "!"

    await context.send(response)


@bot.command()
async def emoji(context):
    await context.send("i don't have nitro :(")


@bot.command()
async def food(context):
    await context.send(random.choice(foodItems))


@bot.command()
async def menu(context):
    embed = discord.Embed(title=context.guild.name + " Menu", description="Seasonal Menu",
                          color=BOT_COLOR)

    for x in range(random.randint(1, 15)):
        foodItem = random.choice(foodItems)
        foodDescription = list(foodItem.replace(':', '').replace('_',' '))
        random.shuffle(foodDescription)
        foodDescription = ''.join(foodDescription).title()
        embed.add_field(name=foodItem + " - " + foodDescription,
                        value="$" + str(random.randint(1, 100)), inline=True)

    await context.send(embed=embed)


@bot.command()
async def claimwaifu(context):
    waifu = context.message.mentions

    if len(waifu) == 0:
        await context.send("Invalid claim. Not like you'd even get anyone anyway.")
        return 0

    waifu = waifu[0].name
    author = context.author.name

    if claims.get(author) == waifu:
        await context.send("You already claimed " + waifu + "!")
        return 0
    else:
        for weeb in claims:
            if waifu in claims[weeb]:
                await context.send("You can't take " + weeb + "'s waifu! What is wrong with you!")
                return 0

    claims[author] = waifu
    await context.send(author + " has claimed " + waifu + ".\n" + "UWU")

@bot.command()
async def waifus(context):
    embed = discord.Embed(title=context.guild.name + " Waifus", description="Absolutely Disgusting",
                          color=BOT_COLOR)

    if len(claims) == 0:
        embed.add_field(name='Nobody has a waifu right now. Hooray!', value=':thinking:')

    for weeb in claims:
        embed.add_field(name=weeb, value='Waifu: ' + claims[weeb], inline=False)

    await context.send(embed=embed)

@bot.command()
async def help(context):
    embed = discord.Embed(title="Bargle Bot", description="Akhil's " + random.choice(botAdj) + " bot." +
                                                          "\nCommands are the following: \n",
                          color=BOT_COLOR)

    embed.add_field(name=COMMAND_PREFIX + "draw [phrase] [fill,] [space,]",
                    value="Draws **phrase** as the combination of **fill** and **space**. " +
                          "\n**fill** text that draws the word, accepts multiple args delimited by commas"
                          "\n**space** fills the space between fill, accepts multiple args delimited by commas" +
                          "\nTry ~draw meme :thinking:,:heart: :flag_in:,:ok_hand:",
                    inline=False)

    embed.add_field(name=COMMAND_PREFIX + "drawline [phrase] [fill,] [space,]",
                    value="Same as **draw** but displays letters horizontally.",
                    inline=False)

    embed.add_field(name=COMMAND_PREFIX + "drawshape [shape] [fill,] [space,]",
                    value="Draws shapes!\n" +
                          "Valid shapes are [" + validShapes + "]",
                    inline=False)

    embed.add_field(name=COMMAND_PREFIX + "hi",
                    value="Friendly greetings!",
                    inline=False)

    embed.add_field(name=COMMAND_PREFIX + "emoji",
                    value=":(",
                    inline=False)

    embed.add_field(name=COMMAND_PREFIX + "food",
                    value="Serves delicious **free** food",
                    inline=False)

    embed.add_field(name=COMMAND_PREFIX + "menu",
                    value="Menu for " + context.guild.name + ". Careful, changes very quickly!",
                    inline=False)

    embed.add_field(name=COMMAND_PREFIX + "claimwaifu [member]",
                    value="Claim another fellow guild member as your waifu. I don't get this sick shit.",
                    inline=False)

    embed.add_field(name=COMMAND_PREFIX + "waifus",
                    value="List of guild waifus. ~kyaaa",
                    inline=False)

    embed.add_field(name=COMMAND_PREFIX + "info",
                    value="General bot information.",
                    inline=False)

    await context.send(embed=embed)


@bot.command()
async def info(context):
    creator = bot.get_user(90508678297313280)

    embed = discord.Embed(title="Bargle Bot", description="Akhil's " + random.choice(botAdj) + " bot.",
                          color=BOT_COLOR)
    embed.add_field(name="Author", value=creator.name)
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    embed.add_field(name="Invite",
                    value="[Bargle Bot](https://discordapp.com/api/oauth2/authorize?client_id=221714409574236160&permissions=329792&scope=bot)")

    await context.send(embed=embed)


bot.run(discord_token.current_token)
