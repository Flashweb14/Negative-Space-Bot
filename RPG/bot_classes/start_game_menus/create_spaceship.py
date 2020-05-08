from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import CREATE_SPACESHIP
from RPG.utilities import check_name_valid, check_name_taken


class SpaceshipCreationMenu(BaseHandler):
    def __init__(self, game):
        super().__init__(game, CREATE_SPACESHIP)

    def show(self, message):
        self.game.bot.send_message(message.chat.id, 'Как будет называться твой космический корабль?')

    def handle(self, message):
        if not check_name_valid(message.text):
            self.game.bot.send_message(message.chat.id,
                                       'Название корабля должно быть длиннее 2 символов и содержать в себе только '
                                       'буквы любого алфавита и цифры. Попробуй другое.')
        elif check_name_taken(self.game, self.game.games, message.text):
            self.game.bot.send_message(message.chat.id,
                                       f'К сожалению, название {message.text} уже занято. Попробуй другое.')
        else:
            self.game.spaceship.name = message.text
            self.game.bot.send_message(message.chat.id,
                                       f'Добро пожаловать в игру, {self.game.player.name}')
            self.game.main_menu.start(message)
