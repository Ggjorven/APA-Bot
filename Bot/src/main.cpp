#include <dpp/dpp.h>
 
#include <cstdint>
#include <string>
#include <fstream>

int main() 
{
	// Token retrieval
	std::string botToken;
	std::ifstream file("Bot/BotToken.txt"); // This file has to be created manually
	std::getline(file, botToken);

	// Bot logic
    dpp::cluster bot(botToken);
 
    bot.on_log(dpp::utility::cout_logger());
 
    bot.on_slashcommand([](const dpp::slashcommand_t& e) 
	{
        if (e.command.get_command_name() == "ping")
            e.reply("Pong!");
    });
 
    bot.on_ready([&bot](const dpp::ready_t& e) 
	{
        if (dpp::run_once<struct register_bot_commands>())
            bot.global_command_create(dpp::slashcommand("ping", "Ping pong!", bot.me.id));
    });
 
    bot.start(dpp::st_wait);
	return 0;
}