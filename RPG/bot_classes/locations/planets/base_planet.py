class BasePlanet:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_info(self):
        return f'*{self.name}*\n' \
               f'{self.description}'

    def start(self, message):
        if self.name not in self.bot_game.players[message.chat.id].opened_planets:
            self.bot_game.players[message.chat.id].opened_planets.append(self.name)
        self.port.start(message)
