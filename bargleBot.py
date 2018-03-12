import discord_token

from clientWrapper import client
from controllers import food, meme, info, test, waifu


@client.event
async def on_ready():
    print('Login successful')
    print('User: ', client.user.name)
    print('ID: ', client.user.id)


client.run(discord_token.test_token)
