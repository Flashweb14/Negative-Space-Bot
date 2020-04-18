class BotBaseHandler:
    def __init__(self, bot_game, game_state):
        self.bot_game = bot_game
        self.game_state = game_state

    def start(self, message):
        self.bot_game.players[message.chat.id].state = self.game_state
        self.show(message)

    def show(self, message):
        pass

    def handle(self, message):
        pass
