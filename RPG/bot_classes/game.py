from RPG.consts.game_states import REGISTRATION
from RPG.bot_classes.main_menu.inventory import Inventory
from RPG.bot_classes.main_menu.inventory_item_info import InventoryItemInfo
from RPG.bot_classes.main_menu.main_menu import MainMenu
from RPG.bot_classes.main_menu.equipment import Equipment
from RPG.bot_classes.start_game_menus.create_player import PlayerCreationMenu
from RPG.bot_classes.start_game_menus.create_spaceship import SpaceshipCreationMenu
from RPG.bot_classes.main_menu.player_profile import PlayerProfile
from RPG.bot_classes.locations.spaceship.spaceship import Spaceship
from RPG.bot_classes.locations.planets.estrad.estrad import Estrad
from RPG.bot_classes.fight_system import FightSystem
from RPG.game_classes.player import Player
from RPG.bot_classes.main_menu.equipment_weapon_info import EquipmentWeaponInfo
from RPG.bot_classes.main_menu.equipment_armor_info import EquipmentArmorInfo


class Game:
    def __init__(self, bot, games):
        self.player = Player(None)
        self.bot = bot
        self.current_location = None
        self.current_planet = None
        self.opened_planets = []
        self.games = games
        self.state = REGISTRATION
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

        self.current_location = self.estrad.colony
        self.planets = [self.estrad]
