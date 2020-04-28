from RPG.bot_classes.base_handler import BaseHandler
from RPG.game_states import REGISTRATION


class PlayerCreationMenu(BaseHandler):
    def __init__(self, game):
        super().__init__(game, REGISTRATION)

    def show(self, message):
        self.game.bot.send_message(message.chat.id, 'Как тебя будут звать?')

    def handle(self, message):
        name_taken = False
        for user_id in self.game.players:
            if message.text == self.game.players[user_id].name:
                name_taken = True
                self.game.bot.send_message(message.chat.id, f'Прости, имя {message.text} уже занято, '
                                                                f'попробуй другое')
        if not name_taken:
            self.game.players[message.chat.id].name = message.text
            self.game.spaceship_creation_menu.start(message)
