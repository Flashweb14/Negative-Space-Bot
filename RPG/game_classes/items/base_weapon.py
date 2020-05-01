from RPG.game_classes.items.base_object import BaseObject


class BaseWeapon(BaseObject):
    def __init__(self, name, damage, ammo_type, price):
        super().__init__(name, 'weapon', price)
        self.damage = damage
        self.ammo_type = ammo_type

    def use(self, player):
        if player.weapon is None:
            player.weapon = self
            player.inventory[player.inventory.index(self)] = None
            player.sort_inventory()
        else:
            player.inventory[player.inventory.index(self)] = player.weapon
            player.weapon = self
        player.inventory.sort()

    def get_info(self):
        info = f'*{self.name}* \n' \
               f'_🗡Урон_: {self.damage} \n' \
               f'_🔋Тип боеприпасов_: {self.ammo_type}'
        return info

    def __str__(self):
        return f'🔫{self.name} 🗡{self.damage}'
