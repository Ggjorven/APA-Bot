import discord
from discord.ext import commands
from dotenv import load_dotenv
from enum import Enum
import typing

from BotEvents import BotEvents
from BotMethods import BotMethods

class Bot:
    class CreateMode(Enum):
        Token = 0
        Path = 1

    def __init__(self, mode: CreateMode, input: str):
        self.token: str | None = None
        self.bot: commands.Bot | None = None

        load_dotenv()

        match mode:
            case Bot.CreateMode.Token:
                self.Create(input)
            case Bot.CreateMode.Path:
                self.Create(Bot.GetToken(input))

        # Initialize events/methods
        BotEvents.Init(self.bot)
        BotMethods.Init(self.bot)
    
    def Create(self, token: str) -> None:
        # Creation
        self.token = token

        intents: discord.Intents = discord.Intents.default()
        intents.messages = True          # Enables message-related events
        intents.message_content = True   # Enables access to message content
        intents.guilds = True            # Enables guild-related events

        self.bot = commands.Bot(command_prefix="!", intents=intents)

    def Run(self) -> None:
        self.bot.run(self.token)

    @staticmethod
    def GetToken(path: str) -> str:
        with open(path) as file:
            return file.readline().strip()