from discord.ext import commands
from assets import defaults
from pymongo import MongoClient

client = commands.Bot(command_prefix=defaults.COMMAND_PREFIX, description="Akhil's loyal bargle bot.")
mongoClient = MongoClient('localhost', 27017)
