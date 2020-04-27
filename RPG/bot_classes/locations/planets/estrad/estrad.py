from RPG.bot_classes.locations.planets.base_planet import BasePlanet
from RPG.bot_classes.locations.planets.estrad.estrad_port import EstradPort
from RPG.bot_classes.locations.planets.estrad.estrad_security_soldier import EstradSecuritySoldier


class Estrad(BasePlanet):
    def __init__(self, bot_game):
        super().__init__('Эстрад',
                         'Это небольшая планета на краю галактики, обладающая тропическим климатом. В данный момент '
                         'планета колонизируется Межгалактической Федерацией. Население планеты представлено '
                         'местными аборигенами, представителями расы Эстрадин, и колонизаторами Межгалактической'
                         'Федерации.')
        self.bot_game = bot_game
        self.port = EstradPort(bot_game, self)
        self.security_soldier = EstradSecuritySoldier(bot_game, self)

    def start(self, message):
        if self.name not in self.bot_game.players[message.chat.id].opened_planets:
            self.bot_game.players[message.chat.id].opened_planets.append(self.name)
        self.port.start(message)
