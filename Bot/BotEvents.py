from discord.ext import commands
import re
import typing

from SourceGen import SourceGen

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
            # Ignore messages from the bot itself
            if message.author == bot.user:
                return

            # Log message details
            print(f"Message from {message.author}: {message.content} (Channel: {message.channel}, ID: {message.id})")

            # Regular expression to find URLs in the message
            url_pattern = re.compile(r'(https?://\S+)')
            urls: list[any] = url_pattern.findall(message.content)

            for url in urls:
                print(f"Found URL: {url}")

                # Call extract_info for each URL and print the result
                source: SourceGen = SourceGen(url)
                print(f"Date Published: {source.GetDatePublished()}")
                print(f"Author: {source.GetAuthor()}")

            # Process commands if there are any
            await bot.process_commands(message)