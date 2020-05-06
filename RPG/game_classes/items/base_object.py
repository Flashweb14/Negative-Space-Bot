class BaseObject:
    def __init__(self, name, info, price):
        self.name = name
        self.info = info
        self.price = price

    def use(self, player):
        pass

    def get_info(self):
        return self.info

    def __str__(self):
        return self.name
