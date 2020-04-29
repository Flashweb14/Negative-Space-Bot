from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import CREATE_SPACESHIP


class SpaceshipCreationMenu(BaseHandler):
    def __init__(self, game):
        super().__init__(game, CREATE_SPACESHIP)

    def show(self, message):
        self.game.bot.send_message(message.chat.id, 'Как будет называться твой космический корабль?')

    def handle(self, message):
        name_taken = False
        for game_id in self.game.games:
            if message.text == self.game.games[game_id].spaceship.name:
                name_taken = True
                self.game.bot.send_message(message.chat.id, f'Прости, название {message.text} уже занято, '
                                                            f'попробуй другое')
        if not name_taken:
            self.game.spaceship.name = message.text
            self.game.bot.send_message(message.chat.id,
                                       f'Добро пожаловать в игру, {self.game.player.name}')
            self.game.main_menu.start(message)
