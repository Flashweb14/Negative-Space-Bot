from RPG.consts.quest_items import FEDERATION_PASS


class Player:
    def __init__(self, name):
        self.chosen_item = None
        self.quest_items = [FEDERATION_PASS]

        self.name = name
        self.hp = 60
        self.armor = 0
        self.level = 1
        self.money = 250

        self.inventory = [None] * 5
        self.weapon = None
        self.armor_set = None

        self.endurance = 1
        self.accuracy = 1
        self.perception = 1
        self.charisma = 1
        self.agility = 1
        self.luck = 1

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
            weapon = '<Пусто>'
        if self.armor_set is None:
            armor_set = '<Пусто>'
        equipment = f'😎*{self.name}*\n' \
                    f'🧥_Комплект брони_: {str(armor_set)[1:]}\n' \
                    f'🔫_Оружие_: {str(weapon)[1:]}'
        return equipment
