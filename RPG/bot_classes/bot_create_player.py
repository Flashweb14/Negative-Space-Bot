from RPG.bot_classes.bot_base_handler import BotBaseHandler
from RPG.game_states import REGISTRATION


class BotPlayerCreationMenu(BotBaseHandler):
    def __init__(self, bot_game):
        super().__init__(bot_game, REGISTRATION)

    def show(self, message):
        self.bot_game.bot.send_message(message.chat.id, 'Как тебя будут звать?')

    def handle(self, message):
        name_taken = False
        for user_id in self.bot_game.players:
            if message.text == self.bot_game.players[user_id].name:
                name_taken = True
                self.bot_game.bot.send_message(message.chat.id, f'Прости, имя {message.text} уже занято, '
                                                                f'попробуй другое')
        if not name_taken:
            self.bot_game.players[message.chat.id].name = message.text
            self.bot_game.bot.send_message(message.chat.id, f'Добро пожаловать в игру, {message.text}')
            self.bot_game.main_menu.start(message)
