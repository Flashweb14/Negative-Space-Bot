from RPG.consts.game_states import CREATE_PLAYER_MENU  # Импортирует старотовое состояние игры
from RPG.bot_classes.start_game_menus.create_player import PlayerCreationMenu  # Импортирует все меню
from RPG.bot_classes.start_game_menus.create_spaceship import SpaceshipCreationMenu
from RPG.game_classes.player import Player
from RPG.bot_classes.fight_system.fight_system import FightSystem
from RPG.bot_classes.main_menu.main_menu import MainMenu
from RPG.bot_classes.main_menu.inventory import Inventory
from RPG.bot_classes.main_menu.inventory_item_info import InventoryItemInfo
from RPG.bot_classes.main_menu.equipment import Equipment
from RPG.bot_classes.main_menu.equipment_weapon_info import EquipmentWeaponInfo
from RPG.bot_classes.main_menu.equipment_armor_info import EquipmentArmorInfo
from RPG.bot_classes.main_menu.player_profile import PlayerProfile
from RPG.bot_classes.locations.spaceship.spaceship import Spaceship  # Импортирует локации
from RPG.bot_classes.locations.planets.estrad.estrad import Estrad
from RPG.saves.data.games import DBGame
from RPG.consts.items import items
from RPG.consts.enemies import enemies


class Game:
    def __init__(self, bot, chat_id, player_name, spaceship_name, current_location, state, player_inventory,
                 player_money, player_hp, player_armor, player_weapon, player_armor_set, player_laser_ammo,
                 fight_system_enemy, player_quest_items, fight_system_max_action_points,
                 fight_system_action_points, games):
        self.player = Player(player_name)
        self.fight_system = FightSystem(self)
        self.fight_system.enemy = enemies[fight_system_enemy]
        self.fight_system.max_action_points = fight_system_max_action_points
        self.fight_system.action_points = fight_system_action_points

        for item_name in player_inventory.split(', '):
            self.player.add_item(items[item_name])
        if player_quest_items:
            self.player.quest_items = [int(item) for item in player_quest_items.split(', ')]
        else:
            self.player.quest_items = []
        self.player.money = player_money
        self.player.hp = player_hp
        self.player.armor = player_armor
        self.player.weapon = items[player_weapon]
        self.player.armor_set = items[player_armor_set]
        self.player.laser_ammo = player_laser_ammo

        self.bot = bot
        self.state = state
        self.games = games  # Словарь всех других игр(необходим для мультиплеера)
        self.chat_id = chat_id
        self.current_planet = None
        self.opened_planets = []

        self.player_creation_menu = PlayerCreationMenu(self)  # Меню создания игрока
        self.spaceship_creation_menu = SpaceshipCreationMenu(self)

        self.main_menu = MainMenu(self)  # Главное меню
        self.inventory = Inventory(self)
        self.inventory_item_info = InventoryItemInfo(self)
        self.player_profile = PlayerProfile(self)
        self.equipment = Equipment(self)
        self.equipment_weapon_info = EquipmentWeaponInfo(self)
        self.equipment_armor_info = EquipmentArmorInfo(self)

        self.spaceship = Spaceship(self)  # Корабль
        self.spaceship.name = spaceship_name
        self.estrad = Estrad(self, self.player)  # Планеты

        self.locations = [self.spaceship, self.estrad]
        self.locations_dictionary = {}
        for location in self.locations:
            self.get_child_locations(location)
        print(self.locations_dictionary)

        self.current_location = self.locations_dictionary[current_location]
        self.planets = [self.estrad]

    def get_child_locations(self, location):
        for location in location.child_locations:
            self.locations_dictionary[location.name] = location
            if location.child_locations:
                self.get_child_locations(location)

    def save(self, session):
        in_db = False
        for _ in session.query(DBGame).filter(DBGame.chat_id == self.chat_id):
            in_db = True
        if in_db:
            game = session.query(DBGame).filter(DBGame.chat_id == self.chat_id).first()
            print('Изменил!')
        else:
            game = DBGame()
            print('Добавил!')
        game.chat_id = self.chat_id
        game.player_name = self.player.name
        game.spaceship_name = self.spaceship.name
        game.current_location = self.current_location.name
        game.state = self.state
        game.player_inventory = self.player.inventory_to_str()
        game.player_money = self.player.money
        game.player_hp = self.player.hp
        game.player_armor = self.player.armor
        game.player_weapon = self.player.weapon_to_str()
        game.player_armor_set = self.player.armor_to_str()
        game.player_laser_ammo = self.player.laser_ammo
        if self.fight_system.enemy:
            game.fight_system_enemy = self.fight_system.enemy.name
        else:
            game.fight_system_enemy = ''
        game.fight_system_max_action_points = self.fight_system.max_action_points
        game.fight_system_action_points = self.fight_system.action_points
        game.player_quest_items = ', '.join([str(item) for item in self.player.quest_items])
        session.add(game)
        session.commit()
