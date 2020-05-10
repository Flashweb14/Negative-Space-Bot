from RPG.bot_classes.locations.planets.estrad.forest.entry import ForestEntry
from RPG.bot_classes.locations.planets.estrad.forest.field import ForestField


class EstradForest:
    def __init__(self, game):
        self.entry = ForestEntry(game)
        self.field = ForestField(game)
