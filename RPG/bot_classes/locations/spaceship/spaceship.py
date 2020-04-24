from RPG.bot_classes.locations.spaceship.cabin import Cabin
from RPG.bot_classes.locations.spaceship.captain_bridge import CaptainBridge
from RPG.bot_classes.locations.spaceship.cargo_hold import CargoHold


class Spaceship:
    def __init__(self, bot_game):
        self.cabin = Cabin(bot_game, self)
        self.captain_bridge = CaptainBridge(bot_game, self)
        self.cargo_hold = CargoHold(bot_game, self)
