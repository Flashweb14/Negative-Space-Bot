from RPG.bot_classes.bot_base_handler import BotBaseHandler


class BaseLocation(BotBaseHandler):
    def __init__(self, bot_game, game_state, name, description):
        super().__init__(bot_game, game_state)
        self.name = name
        self.description = description
        self.show_message = f'*{self.name}*\n' \
                            f'{self.description}'

    def start(self, message):
        self.bot_game.players[message.chat.id].state = self.game_state
        self.bot_game.players[message.chat.id].current_location = self
        self.show(message)

    def show(self, message):
        pass

    def handle(self, message):
        pass