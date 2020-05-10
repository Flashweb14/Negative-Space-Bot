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


class Game:
    def __init__(self, bot, games):
        self.bot = bot
        self.state = CREATE_PLAYER_MENU
        self.games = games  # Словарь всех других игр(необходим для мультиплеера)
        self.current_location = None
        self.current_planet = None
        self.opened_planets = []

        self.player = Player(None)
        self.fight_system = FightSystem(self)

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

        self.estrad = Estrad(self, self.player)  # Планеты

        self.current_location = self.spaceship.cabin
        self.planets = [self.estrad]
