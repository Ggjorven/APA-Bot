import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Read the bot token from the file
with open('BotToken.txt', 'r') as file:
    TOKEN = file.readline().strip()

# Define intents
intents = discord.Intents.default()
intents.guilds = True  # Enables guild-related events

# Create a bot with the specified intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Sync commands on bot start
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:
        print(f'Connected to guild: {guild.name} (id: {guild.id})')
    # Sync the commands globally or for specific guilds
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s) globally.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Define a simple slash command
@bot.tree.command(name="hello", description="Says hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.display_name}!")

# Run the bot with the token
bot.run(TOKEN)
