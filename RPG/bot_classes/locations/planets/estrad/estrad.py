from RPG.bot_classes.locations.planets.base_planet import BasePlanet
from RPG.bot_classes.locations.planets.estrad.estrad_port import EstradPort
from RPG.bot_classes.locations.planets.estrad.estrad_security_soldier import EstradSecuritySoldier
from RPG.bot_classes.locations.planets.estrad.estrad_colony import EstradColony
from RPG.bot_classes.locations.planets.estrad.estrad_trader import EstradTrader


class Estrad(BasePlanet):
    def __init__(self, game, player):
        super().__init__('Эстрад',
                         'Это небольшая планета на краю галактики, обладающая тропическим климатом. В данный момент '
                         'планета колонизируется Межгалактической Федерацией. Население планеты представлено '
                         'местными аборигенами, представителями расы Эстрадин, и колонизаторами Межгалактической'
                         'Федерации.')
        self.game = game
        self.player = player
        self.port = EstradPort(game)
        self.security_soldier = EstradSecuritySoldier(game, self.player)
        self.colony = EstradColony(game)
        self.trader = EstradTrader(game)

    def start(self, message):
        if self not in self.game.opened_planets:
            self.game.opened_planets.append(self)
        self.port.start(message)
