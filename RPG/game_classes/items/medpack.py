from RPG.game_classes.items.base_object import BaseObject


class MedPack(BaseObject):
    def __init__(self, name, hp_increase):
        info = f'*➕{name}*\n' \
               f'❤_️Восстанавливает {hp_increase} едениц здоровья._'
        super().__init__(name, info, 100)
        self.hp_increase = hp_increase

    def use(self, player):
        player.hp += self.hp_increase
        if player.hp > 100:
            player.hp = 100
        player.inventory[player.inventory.index(self)] = None
        player.inventory.sort()

    def __str__(self):
        return f'➕{self.name}'
