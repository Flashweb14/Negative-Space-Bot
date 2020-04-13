from RPG.game_classes.base_object import BaseObject


class BaseWeapon(BaseObject):
    def __init__(self, name, damage, durability, ammo_type, price):
        super().__init__(name, 'weapon', price)
        self.damage = damage
        self.durability = durability[0]
        self.max_durability = durability[1]
        self.ammo_type = ammo_type
