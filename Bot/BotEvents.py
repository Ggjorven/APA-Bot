from discord.ext import commands
import typing

class BotEvents:
    @staticmethod
    def Init(bot: commands.Bot) -> None:
        # Initialization event
        @bot.event
        async def on_ready() -> None:
            print(f'{bot.user} has connected to Discord!')

            for guild in bot.guilds:
                print(f'Connected to guild: {guild.name} (id: {guild.id})')
            
            # Sync the commands globally
            try:
                print(f"Synced {len(await bot.tree.sync())} command(s) globally.")
            except Exception as e:
                print(f"Failed to sync commands: {e}")

        # Parse messages
        @bot.event
        async def on_message(message) -> None:
            if message.author == bot.user:
                return

            print(f"Message from {message.author}: {message.content} (Channel: {message.channel}, ID: {message.id})")

            # If the message was a command, wait for it to finish
            await bot.process_commands(message)