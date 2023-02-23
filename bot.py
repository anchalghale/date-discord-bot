import discord
from discord.ext import commands

import settings

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=settings.COMMANDS_PREFIX, intents=intents)
bot.remove_command('help')
