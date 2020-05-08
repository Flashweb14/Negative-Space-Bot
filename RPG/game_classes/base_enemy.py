class BaseEnemy:
    def __init__(self, name, fight_message, hp, damage, accuracy, perception, luck, agility):
        self.name = name
        self.fight_message = fight_message
        self.hp = hp
        self.weapon = damage
        self.accuracy = accuracy
        self.perception = perception
        self.luck = luck
        self.agility = agility
