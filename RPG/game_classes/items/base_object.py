class BaseObject:
    def __init__(self, name, type, price):
        self.name = name
        self.price = price
        self.type = type

    def use(self, player):
        pass

    def get_info(self):
        pass

    def __str__(self):
        return self.name
