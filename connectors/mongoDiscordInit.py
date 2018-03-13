"""
**************************************WARNING**************************************
Running this file with an active MongoDB instance will wipe everything.
This requires a discord bot to be in a server/guild.
Use this for initialization only. Or do whatever you want, not like I care. B-baka!
"""

from utils.clientWrapper import mongoClient, client
import discord_token
import pymongo


@client.event
async def on_ready():
    print('Login successful')
    print('User: ', client.user.name)
    print('ID: ', client.user.id)

    db = mongoClient['bargleDB']
    guildsDB = mongoClient['bargleDB']['guilds']
    storesDB = mongoClient['bargleDB']['stores']
    waifusDB = mongoClient['bargleDB']['waifus']
    inventoryDB = mongoClient['bargleDB']['inventory']

    guildsDB.create_index([('guildId', pymongo.ASCENDING)],
                          unique=True)
    storesDB.create_index([('guildId', pymongo.ASCENDING)],
                          unique=True)
    waifusDB.create_index([('guildId', pymongo.ASCENDING)],
                          unique=True)
    inventoryDB.create_index([('guildId', pymongo.ASCENDING)],
                             unique=True)
    inventoryDB.create_index([('guildId.memberId', pymongo.ASCENDING)],
                             unique=True)
    guilds = []
    inventory = []
    stores = []

    for guild in client.guilds:
        guildData = {
            'guildId': guild.id,
            'members': []
        }
        storeData = {
            'guildId': guild.id,
            'store': {

            }
        }

        for member in guild.members:
            memberData = {
                'name': member.name,
                'id': member.id
            }

            guildData['members'].append(memberData)

        guilds.append(guildData)

    guildsDB.insert_many(guilds)

    mongoClient.close()
    client.close()


client.run(discord_token.test_token)
