from RPG.consts.quest_items import FEDERATION_PASS


class Player:
    def __init__(self, name):
        self.chosen_item = None
        self.quest_items = [FEDERATION_PASS]

        self.name = name
        self.hp = 60
        self.weapon = None
        self.inventory = [None] * 5
        self.level = 1
        self.money = 250

        self.strength = 3
        self.perception = 4
        self.endurance = 5
        self.charisma = 10
        self.intelligence = 7
        self.agility = 6
        self.luck = 7

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
                self.money -= item.price // trader_factor
                return True, 'Успешно куплено:'
        else:
            return False, 'недостаточно денег'

    def drop_item(self, item):
        self.inventory[self.inventory.index(item)] = None
        self.sort_inventory()

    def sort_inventory(self):
        for i in range(len(self.inventory)):
            if i != 0:
                if self.inventory[i - 1] is None:
                    self.inventory[i - 1] = self.inventory[i]
                    self.inventory[i] = None
