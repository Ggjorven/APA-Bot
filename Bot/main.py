import Bot as APA

if __name__ == '__main__':
    bot: APA.Bot = APA.Bot(APA.Bot.CreateMode.Path, "BotToken.txt")
    bot.Run()