from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import REGISTRATION
from RPG.utilities import check_name_valid, check_player_name_taken


class PlayerCreationMenu(BaseHandler):
    def __init__(self, game):
        super().__init__(game, REGISTRATION)

    def show(self, message):
        self.game.bot.send_message(message.chat.id, 'Как тебя будут звать?')

    def handle(self, message):
        if not check_name_valid(message.text):
            self.game.bot.send_message(message.chat.id, 'Имя должно быть длиннее 2 символов и содержать в себе только '
                                                        'буквы любого алфавита и цифры. Попробуй другое.')
        elif check_player_name_taken(self.game.games, message.text):
            self.game.bot.send_message(message.chat.id, f'К сожалению, имя {message.text} уже занято. Попробуй другое.')
        else:
            self.game.player.name = message.text
            self.game.spaceship_creation_menu.start(message)
