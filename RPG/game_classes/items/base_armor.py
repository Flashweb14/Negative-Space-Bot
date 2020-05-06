from RPG.game_classes.items.base_object import BaseObject


class BaseArmorSet(BaseObject):
    def __init__(self, name, armor, price):
        info = f'🧥*{name}* \n' \
               f'🛡_Защита_: {armor} \n'
        super().__init__(name, info, price)
        self.armor = armor

    def use(self, player):
        if player.armor_set is None:
            player.armor += self.armor
            player.armor_set = self
            player.inventory[player.inventory.index(self)] = None
            player.sort_inventory()
        else:
            player.armor -= player.armor_set.armor
            player.armor += self.armor
            player.inventory[player.inventory.index(self)] = player.armor_set
            player.armor_set = self

    def __str__(self):
        return f'🧥{self.name} 🛡{self.armor}'
