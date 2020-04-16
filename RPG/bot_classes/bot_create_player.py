from RPG.game_classes.game import Game
from RPG.bot_classes.bot_base_handler import BotBaseHandler
from RPG.consts import NONE_STATE


class BotPlayerCreationMenu(BotBaseHandler):
    def __init__(self, bot_game):
        super().__init__(bot_game)

    def show(self, message):
        self.bot_game.bot.send_message(message.chat.id, 'Как тебя будут звать?')

    def handler(self, message):
        name_taken = False
        for user in self.bot_game.games:
            if message.text == self.bot_game.games[user].player.name:
                name_taken = True
                self.bot_game.bot.send_message(message.chat.id, f'Прости, имя {message.text} уже занято,'
                                                                f'попробуй другое')
        if not name_taken:
            self.bot_game.games[message.chat.id].player.name = message.text
            self.bot_game.games[message.chat.id].state = NONE_STATE
            self.bot_game.bot.send_message(message.chat.id, f'Добро пожаловать в игру, {message.text}')
