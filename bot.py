import os
import asyncio
import discord
import random

from os import getenv
from discord.ext import commands
from PIL import Image
from dotenv import load_dotenv
load_dotenv(override=True)

PREFIX = "!"  # Define your command prefix here
OWNER_IDS = {123456789012345678, 987654321098765432}  # Replace with actual owner IDs

client = commands.Bot(
    command_prefix=PREFIX,
    owner_ids=OWNER_IDS,
    intents=discord.Intents.all(),
    help_command=None  # Disable the default help command
)

COG_FOLDER = './cogs'  # Define the folder where your cogs are located

async def load_all_extensions():
    for filename in os.listdir(COG_FOLDER):
        if filename.endswith('.py'):
            extension = f'cogs.{filename[:-3]}'
            if extension not in client.extensions:
                try:
                    await client.load_extension(extension)
                    print(f'Loaded extension {extension}')
                except commands.errors.ExtensionAlreadyLoaded:
                    print(f'Extension {extension} is already loaded.')
                except Exception as e:
                    print(f'Failed to load extension {extension}: {e}')

extensions = [
    'cogs.games',
    'cogs.player',
    'cogs.mining',
    'cogs.help',
    'cogs.guild',
    'cogs.gambling',
    'cogs.gambling_helpers',  # Added new extension
    'cogs.help_commands'  # Added new extension
]

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    await load_all_extensions()

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

@client.command()
async def roll_dice(ctx):
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

async def load_extensions(client, extensions):
    for extension in extensions:
        try:
            await client.load_extension(extension)
            print(f'Loaded extension {extension}')
        except Exception as e:
            print(f'Failed to load extension {extension}: {e}')

async def main():
    token = getenv('TOKEN')
    if not token:
        print("Error: TOKEN environment variable not set.")
        return

    try:
        await load_all_extensions()
        await client.start(token)
    except KeyboardInterrupt:
        await client.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program interrupted by user")