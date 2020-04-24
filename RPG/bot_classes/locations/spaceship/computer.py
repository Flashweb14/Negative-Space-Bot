from telebot.types import ReplyKeyboardMarkup
from time import sleep
from datetime import datetime
from RPG.game_states import COMPUTER
from RPG.bot_classes.bot_base_handler import BotBaseHandler


class Computer(BotBaseHandler):
    def __init__(self, bot_game, spaceship):
        super().__init__(bot_game, COMPUTER)
        self.spaceship = spaceship

    def show(self, message):
        self.bot_game.bot.send_message(message.chat.id, "Ты подходишь к бортовому компьютеру и запускаешь его")
        sleep(1)
        self.bot_game.bot.send_message(message.chat.id, "_Spaceship Minisoft console: starting._",
                                       parse_mode='Markdown')
        sleep(1)
        self.bot_game.bot.send_message(message.chat.id, "_Loading..._",
                                       parse_mode='Markdown')
        sleep(2)
        self.bot_game.bot.send_message(message.chat.id,
                                       f"_Spaceship Minisoft console 3.8.2 _ {str(datetime.today())[:-7]}",
                                       parse_mode='Markdown')
        self.bot_game.bot.send_message(message.chat.id, '_Type "help" command to get the command list_',
                                       parse_mode='Markdown')

    def handle(self, message):
        if message.text == 'help':
            self.bot_game.bot.send_message(message.chat.id,
                                           '*ftp --ls -n <PLANET NAME>* _- set route to the chosen planet_ \n'
                                           '*sps qm --inf -m* _- check spaceship equipment and info_ \n'
                                           '*q* _- close Spaceship Minisoft console_',
                                           parse_mode='Markdown')
        elif message.text == 'q':
            self.bot_game.bot.send_message(message.chat.id, '_Closing terminal..._',
                                           parse_mode='Markdown')
            sleep(1)
            self.bot_game.bot.send_message(message.chat.id, '_Process finished with exit code -1_',
                                           parse_mode='Markdown')
            sleep(1)
            self.spaceship.captain_bridge.start(message)