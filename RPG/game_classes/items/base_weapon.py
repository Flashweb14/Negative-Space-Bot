from RPG.game_classes.items.base_object import BaseObject


class BaseWeapon(BaseObject):
    def __init__(self, name, damage, loaded_ammo, max_ammo, price):
        self.max_ammo = max_ammo
        self.loaded_ammo = loaded_ammo
        self.info = f'🔫*{name}* \n' \
                    f'_🗡Урон_: {damage} \n' \
                    f'_🔋Магазин_: {self.loaded_ammo}/{self.max_ammo}\n'
        super().__init__(name, self.info, price)
        self.damage = damage

    def reload(self):
        self.loaded_ammo = self.max_ammo
        self.info = f'🔫*{self.name}* \n' \
                    f'_🗡Урон_: {self.damage} \n' \
                    f'_🔋Магазин_: {self.loaded_ammo}/{self.max_ammo}\n'
        return f'{self.name} успешно перезаряжено!'

    def use(self, player):
        if player.weapon is None:
            player.weapon = self
            player.inventory[player.inventory.index(self)] = None
            player.sort_inventory()
        else:
            player.inventory[player.inventory.index(self)] = player.weapon
            player.weapon = self

    def __str__(self):
        return f'🔫{self.name} 🗡{self.damage}'
