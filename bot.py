# Marshall Ferguson - 11/2020

# Imports

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(help="tYpE '!sarcasm' fOlLoWeD bY tHe TeXt To MiMiC")
async def sarcasm(ctx, *, message):

    sarcatic_message = ''
    condition = True
    for letter in message:
        if condition:
            sarcatic_message += letter.upper()
        else:
            sarcatic_message += letter.lower()
        if letter != ' ':
            condition = not condition
    await ctx.send(sarcatic_message)

bot.run(TOKEN)
