class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.weapon = None
        self.inventory = [None] * 5
        self.level = 1

        self.strength = 3
        self.perception = 4
        self.endurance = 5
        self.charisma = 8
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
        if not added_item:
            print('Инвентарь полон!')

    def equip_weapon(self, weapon):
        if self.weapon is None:
            self.weapon = weapon
            self.inventory[self.inventory.index(weapon)] = None
            self.sort_inventory()
        else:
            self.inventory[self.inventory.index(weapon)] = self.weapon
            self.weapon = weapon

    def drop_item(self, item):
        self.inventory[self.inventory.index(item)] = None
        self.sort_inventory()

    def sort_inventory(self):
        for i in range(len(self.inventory)):
            if i != 0:
                if self.inventory[i - 1] is None:
                    self.inventory[i - 1] = self.inventory[i]
                    self.inventory[i] = None
