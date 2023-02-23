import commands
import settings
from bot import bot
from logger import logger


@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
    except Exception as e:
        logger.error(e)


def main():
    bot.run(settings.BOT_TOKEN)


if __name__ == '__main__':
    main()
