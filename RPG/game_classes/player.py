class Player:
    def __init__(self):
        self.hp = 20
        self.weapon = None
        self.inventory = [None] * 10

    def add_item(self, item):
        added_item = False
        for i in range(len(self.inventory)):
            if self.inventory[i] is None:
                self.inventory[i] = item
                added_item = True
                break
        if not added_item:
            print('Инвентарь полон!')
