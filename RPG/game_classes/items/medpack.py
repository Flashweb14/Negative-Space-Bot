from RPG.game_classes.items.base_object import BaseObject


class MedPack(BaseObject):
    def __init__(self, name, hp_increase):
        super().__init__(name, 'item', 100)
        self.hp_increase = hp_increase

    def use(self, player):
        player.hp += self.hp_increase
        if player.hp > 100:
            player.hp = 100
        player.inventory[player.inventory.index(self)] = None
        player.inventory.sort()

    def get_info(self):
        return f'*➕{self.name}*\n' \
               f'❤_️Восстанавливает {self.hp_increase} едениц здоровья._'

    def __str__(self):
        return f'➕{self.name}'
