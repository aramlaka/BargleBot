import discord

from utils.clientWrapper import client

@client.command()
async def guilds(context):
    for guild in client.guilds:
        await context.send("Name: " + guild.name + '\nID: ' + str(guild.id))

# @client.event
# async def on_context(context):
#    if any(emoji in context.content for emoji in ['👖']):
#        channel = context.channel
#        embed = discord.Embed(title='🦆👖', color=CLIENT_COLOR)
#        embed.add_field(name='ohno', value='https://www.youtube.com/watch?v=1PaKYvMdH3o')
#        await channel.send(embed=embed)