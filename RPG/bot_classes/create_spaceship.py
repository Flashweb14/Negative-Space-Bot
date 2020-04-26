from RPG.bot_classes.bot_base_handler import BotBaseHandler
from RPG.game_states import CREATE_SPACESHIP


class SpaceshipCreationMenu(BotBaseHandler):
    def __init__(self, bot_game):
        super().__init__(bot_game, CREATE_SPACESHIP)

    def show(self, message):
        self.bot_game.bot.send_message(message.chat.id, 'Как будет называться твой космический корабль?')

    def handle(self, message):
        name_taken = False
        for spaceship_id in self.bot_game.spaceship:
            if message.text == self.bot_game.spaceship[spaceship_id].name:
                name_taken = True
                self.bot_game.bot.send_message(message.chat.id, f'Прости, название {message.text} уже занято, '
                                                                f'попробуй другое')
        if not name_taken:
            self.bot_game.spaceship[message.chat.id].name = message.text
            self.bot_game.bot.send_message(message.chat.id,
                                           f'Добро пожаловать в игру, {self.bot_game.players[message.chat.id].name}')
            self.bot_game.main_menu.start(message)
