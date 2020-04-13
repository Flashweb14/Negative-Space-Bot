from RPG.game_classes.player import Player


class Game:
    def __init__(self):
        self.player = Player()
        self.inventory_opened = False
        self.chosen_item = None
