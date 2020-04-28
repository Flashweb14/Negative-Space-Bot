from RPG.bot_classes.main_menu.inventory import Inventory
from RPG.bot_classes.main_menu.inventory_item_info import InventoryItemInfo
from RPG.bot_classes.main_menu.main_menu import MainMenu
from RPG.bot_classes.start_game_menus.create_player import PlayerCreationMenu
from RPG.bot_classes.start_game_menus.create_spaceship import SpaceshipCreationMenu
from RPG.bot_classes.main_menu.player_profile import PlayerProfile
from RPG.bot_classes.locations.spaceship.spaceship import Spaceship
from RPG.bot_classes.locations.planets.estrad.estrad import Estrad
from RPG.game_classes.player import Player


class Game:
    def __init__(self, bot):
        self.players = {}
        self.bot = bot
        self.player_creation_menu = PlayerCreationMenu(self)
        self.spaceship_creation_menu = SpaceshipCreationMenu(self)
        self.main_menu = MainMenu(self)
        self.inventory = Inventory(self)
        self.inventory_item_info = InventoryItemInfo(self)
        self.player_profile = PlayerProfile(self)

        self.spaceship = {}
        self.estrad = {}

        self.planets = [self.estrad]

    def start_new_game(self, command):
        self.players[command.chat.id] = Player(None)

        self.spaceship[command.chat.id] = Spaceship(self)
        self.estrad[command.chat.id] = Estrad(self)

        self.players[command.chat.id].current_location = self.estrad[command.chat.id].port
