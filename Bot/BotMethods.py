import discord
from discord.ext import commands
import typing

class BotMethods:
    @staticmethod
    def Init(bot: commands.Bot) -> None:
        # Test Command
        @bot.tree.command(name="hello", description="Says hello!")
        async def hello(interaction: discord.Interaction):
            await interaction.response.send_message(f"Hello, {interaction.user.display_name}!")