class BaseHandler:
    def __init__(self, game, game_state):
        self.game = game
        self.game_state = game_state

    def start(self, message):
        self.game.players[message.chat.id].state = self.game_state
        self.show(message)

    def show(self, message):
        pass

    def handle(self, message):
        pass
