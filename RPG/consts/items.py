from RPG.game_classes.items.base_weapon import BaseWeapon
from RPG.game_classes.items.medpack import MedPack
from RPG.game_classes.items.base_armor import BaseArmorSet


LITTLE_MED_PACK = MedPack('Малый медицинский пакет', 10)

LIGHT_SOLDIER_ARMOR_SET = BaseArmorSet('Лёгкая солдатская броня', 10, 700)

LIGHT_LASER_RIFFLE = BaseWeapon('Лёгкая лазерная винтовка', 10, 3, 5, 500)
OLD_LASER_PISTOL = BaseWeapon('Поношенный лазерный пистолет', 12, 4, 7, 100)
