from RPG.bot_classes.locations.planets.base_planet import BasePlanet
from RPG.bot_classes.locations.planets.estrad.estrad_port import EstradPort
from RPG.bot_classes.locations.planets.estrad.estrad_security_soldier import EstradSecuritySoldier


class Estrad(BasePlanet):
    def __init__(self, game):
        super().__init__('Эстрад',
                         'Это небольшая планета на краю галактики, обладающая тропическим климатом. В данный момент '
                         'планета колонизируется Межгалактической Федерацией. Население планеты представлено '
                         'местными аборигенами, представителями расы Эстрадин, и колонизаторами Межгалактической'
                         'Федерации.')
        self.game = game
        self.port = EstradPort(game, self)
        self.security_soldier = EstradSecuritySoldier(game, self)

    def start(self, message):
        if self.name not in self.game.players[message.chat.id].opened_planets:
            self.game.players[message.chat.id].opened_planets.append(self.name)
        self.port.start(message)
