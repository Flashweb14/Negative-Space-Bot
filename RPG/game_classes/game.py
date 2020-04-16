from RPG.game_classes.player import Player
from RPG.consts import ZERO_STATE


class Game:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.inventory_opened = False
        self.chosen_item = None
        self.state = ZERO_STATE
