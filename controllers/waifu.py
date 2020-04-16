from clientWrapper import client

import discord
import defaults
import redis

claims = {}

r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('waifus', {'waifu':'gay'})

@client.command()
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


@client.command()
async def waifus(context):
    embed = discord.Embed(title=context.guild.name + " Waifus", description="Absolutely Disgusting",
                          color=defaults.CLIENT_COLOR)

    if len(claims) == 0:
        embed.add_field(name='Nobody has a waifu right now. Hooray!', value=':thinking:')

    for weeb in claims:
        embed.add_field(name=weeb, value='Waifu: ' + claims[weeb], inline=False)

    await context.send(embed=embed)

@client.command()
async def succ(context):
    await context.send(str(dict(r.get('waifus'))['waifu']))
