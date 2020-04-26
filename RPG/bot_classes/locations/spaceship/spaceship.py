from RPG.bot_classes.locations.spaceship.cabin import Cabin
from RPG.bot_classes.locations.spaceship.captain_bridge import CaptainBridge
from RPG.bot_classes.locations.spaceship.cargo_hold import CargoHold
from RPG.bot_classes.locations.spaceship.computer import Computer


class Spaceship:
    def __init__(self, bot_game):
        self.name = "NAME"
        self.hp = 100
        self.cargo = 0

        self.cabin = Cabin(bot_game, self)
        self.captain_bridge = CaptainBridge(bot_game, self)
        self.cargo_hold = CargoHold(bot_game, self)
        self.computer = Computer(bot_game, self)

    def get_info(self):
        info = f'🚀*{self.name}*\n' \
               f'💙_Прочность_: {self.hp}/100\n' \
               f'📦_Грузовой отсек_: {self.cargo}/100'
        return info
