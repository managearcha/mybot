import os
import asyncio
import discord
import random

from os import getenv
from discord.ext import commands
from PIL import Image
from dotenv import load_dotenv
load_dotenv(override=True)

# Check if TOKEN and PREFIX are set
if not getenv('TOKEN'):
    raise ValueError("Error: TOKEN environment variable not set.")
if not getenv('PREFIX'):
    raise ValueError("Error: PREFIX environment variable not set.")

bot = commands.Bot(
    command_prefix=(getenv('PREFIX')),
    intents=discord.Intents.all()
)

bot.remove_command('help')

extensions = [
    'cogs.games',
    'cogs.player',
    'cogs.mining',
    'cogs.help',
    'cogs.guild'
]

async def load_extensions(bot, extensions):
    for extension in extensions:
        await bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

number_abbreviations = {
    1_000: 'k',
    1_000_000: 'm',
    1_000_000_000: 'g',
    1_000_000_000_000: 't',
    1_000_000_000_000_000: 'p',
    1_000_000_000_000_000_000: 'e',
    1_000_000_000_000_000_000_000: 'z',
    1_000_000_000_000_000_000_000_000: 'y'
}

def abbreviate_number(number):
    for value, abbreviation in sorted(number_abbreviations.items(), reverse=True):
        if number >= value:
            return f'{number // value}{abbreviation}'
    return str(number)

@bot.command()
async def roll(ctx):
    roll_result = random.randint(1, 99)
    await ctx.send(f'You rolled a {roll_result}')
    
    rewards = {
        42: (600000, 6),
        21: (300000, 3),
        63: (900000, 9),
        84: (1200000, 12)
    }
    
    if roll_result in rewards:
        reward, multiplier = rewards[roll_result]
    elif 1 <= roll_result <= 20:
        reward = 100000
        multiplier = 1
    elif 22 <= roll_result <= 41:
        reward = 200000
        multiplier = 2
    elif 43 <= roll_result <= 62:
        reward = 300000
        multiplier = 3
    elif 64 <= roll_result <= 83:
        reward = 400000
        multiplier = 4
    else:
        reward = 0
        multiplier = 0

    if reward > 0:
        abbreviated_reward = abbreviate_number(reward)
        await ctx.send(f'You win! Your reward is {abbreviated_reward} with a multiplier of {multiplier}x.')
    else:
        await ctx.send('You lose!')

async def main():
    token = getenv('TOKEN')
    if not token:
        print("Error: TOKEN environment variable not set.")
        return

    try:
        await load_extensions(bot, extensions)
        await bot.start(token)
    except KeyboardInterrupt:
        await bot.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program interrupted by user")