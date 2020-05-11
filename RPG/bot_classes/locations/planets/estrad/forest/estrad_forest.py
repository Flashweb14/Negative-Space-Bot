from RPG.bot_classes.locations.planets.estrad.forest.estrad_forest_entry import ForestEntry
from RPG.bot_classes.locations.planets.estrad.forest.estrad_forest_field import ForestField
from RPG.bot_classes.locations.planets.estrad.forest.estrad_forest_lake import ForestLake


class EstradForest:
    def __init__(self, game):
        self.name = 'Лес на Эстраде'
        self.entry = ForestEntry(game)
        self.field = ForestField(game)
        self.lake = ForestLake(game)
        self.child_locations = [self.entry, self.field, self.lake]
