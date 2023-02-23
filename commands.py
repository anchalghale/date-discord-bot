
import discord
from discord import app_commands

from bot import bot
from converter import convert_to_bs


def get_error_response():
    return {
        'embed': discord.Embed(
            title='Error', description='Some error occured. Make sure the date is valid. Please try again.', colour=discord.Colour.red()),
        'content': None,
    }


def get_date_response(date):
    embed = discord.Embed()
    embed.add_field(name='Date in AD', value=date[0], inline=False)
    embed.add_field(name='Date in BS',  value=date[1], inline=False)
    return {
        'embed': embed,
        'content': None,
    }


@bot.tree.command(name='help', description='Get help.')
async def help(interaction: discord.Interaction):
    embed = discord.Embed(
        title='Help', description='Discord bot to convert AD date to BS(Nepali) date.')
    embed.add_field(name='/date', value="Returns today's date in BS", inline=False)
    embed.add_field(name='/date <yyyy-mm-dd>', value='Convert given AD date to BS.', inline=False)
    await interaction.response.send_message(content=None, embed=embed, ephemeral=True)


@bot.tree.command(name='date', description='Nepali date chahiyo.')
@app_commands.describe(date='Options: today | tomorrow | yesterday | <yyyy-mm-dd>')
async def date(interaction: discord.Interaction, date: str = None):
    converted = convert_to_bs(date=date)
    if converted is None:
        resp = get_error_response()
    else:
        resp = get_date_response(converted)
    await interaction.response.send_message(**resp, ephemeral=True)
