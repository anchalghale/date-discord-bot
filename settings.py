import os

from dotenv import load_dotenv

load_dotenv()


# BOT
BOT_TOKEN = os.environ.get('BOT_TOKEN')
COMMANDS_PREFIX = os.environ.get('COMMANDS_PREFIX', '/')
