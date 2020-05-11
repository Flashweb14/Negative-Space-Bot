from random import randint
from RPG.consts.items import items


class Player:
    def __init__(self, name):
        self.name = name  # Основные характеристики игрока
        self.hp = 60
        self.armor = 0
        self.level = 1
        self.money = 250

        self.endurance = 1  # Индивидуальные параметры игрока
        self.accuracy = 6
        self.perception = 1
        self.charisma = 1
        self.agility = 1
        self.luck = 4

        self.quest_items = []  # Список полученных квестовых предметов

        self.inventory = [None] * 5  # Инвентарь и снаряжение
        self.weapon = None
        self.armor_set = None
        self.laser_ammo = 0

        self.in_fight = False  # Находится ли игрок в бою

    def get_stats(self):
        stats = f'*{self.name}* 😎\n' \
                f'🎖 _Уровень_: {self.level}\n' \
                f'❤ _Здоровье_: {self.hp}\n' \
                f'💵 _Кредиты_: {self.money}\n' \
                f'*Характеристики*\n' \
                f'🔫 _Меткость_: {self.accuracy}\n' \
                f'👂🏻 _Восприятие_: {self.perception}\n' \
                f'🏃🏻‍♂ _Выносливость_: {self.endurance}\n' \
                f'🗣 _Харизма_: {self.charisma}\n' \
                f'🏃🏻‍♂ _Ловкость_: {self.agility}\n' \
                f'🍀 _Удача_: {self.luck}'
        return stats

    def add_item(self, item):
        added_item = False
        for i in range(len(self.inventory)):
            if self.inventory[i] is None:
                self.inventory[i] = item
                added_item = True
                break
        return added_item

    def buy_item(self, item, trader_factor):
        if self.money >= item.price:
            if not self.add_item(item):
                return False, 'инвентарь полон'
            else:
                self.money -= int(item.price * trader_factor)
                return True, 'Успешно куплено:'
        else:
            return False, 'недостаточно денег'

    def sell_item(self, item, trader_factor):
        self.money += int(item.price / trader_factor)
        self.inventory.remove(item)

    def drop_item(self, item):
        self.inventory[self.inventory.index(item)] = None
        self.sort_inventory()

    def sort_inventory(self):
        for i in range(len(self.inventory)):
            if i != 0:
                if self.inventory[i - 1] is None:
                    self.inventory[i - 1] = self.inventory[i]
                    self.inventory[i] = None

    def get_equipment(self):
        weapon, armor_set = self.weapon, self.armor_set
        if self.weapon is None:
            weapon = ' <Пусто>'
        if self.armor_set is None:
            armor_set = ' <Пусто>'
        equipment = f'😎 *{self.name}*\n' \
                    f'🧥 _Комплект брони_: {str(armor_set)[1:]}\n' \
                    f'🔫 _Оружие_: {str(weapon)[1:]}\n' \
                    f'🔋 _Лазерные батареи_: {self.laser_ammo}'
        return equipment

    def attack(self, enemy, shot_accuracy, shot_damage_coef):
        if randint(0, 19) in range(self.accuracy + shot_accuracy):
            if randint(0, 9) in range(self.luck):
                enemy.hp -= self.weapon.damage * 3
                return f'Критическое попадание, ты наносишь противнику ' \
                       f'урон в {self.weapon.damage * 3 * shot_damage_coef} hp'
            else:
                enemy.hp -= self.weapon.damage * shot_damage_coef
                return f'Попадание! Ты нанасошь противнику урон в {self.weapon.damage * shot_damage_coef} hp'

        else:
            if randint(0, 9) not in range(self.luck):
                self.hp -= self.weapon.damage
                return f'Критический промах! Ты попадаешь ' \
                       f'себе в ногу и наносишь урон в размере {self.weapon.damage * shot_damage_coef} hp'
            return 'Промах!'

    def inventory_to_str(self):
        inventory = []
        for item in self.inventory:
            if item is not None:
                for item_name in items:
                    if items[item_name] == item:
                        inventory.append(item_name)
        return ', '.join(inventory)

    def weapon_to_str(self):
        weapon_name = None
        for item_name in items:
            if items[item_name] == self.weapon:
                weapon_name = item_name
        return weapon_name

    def armor_to_str(self):
        armor_name = None
        for item_name in items:
            if items[item_name] == self.armor_set:
                armor_name = item_name
        return armor_name
