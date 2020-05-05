class BaseEnemy:
    def __init__(self, name, fight_message, hp, weapon, perception, luck, agility):
        self.name = name
        self.fight_message = fight_message
        self.hp = hp
        self.weapon = weapon
        self.perception = perception
        self.luck = luck
        self.agility = agility
