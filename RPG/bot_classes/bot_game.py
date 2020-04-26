from RPG.bot_classes.bot_inventory import BotInventory
from RPG.bot_classes.bot_inventory_item_info import BotInventoryItemInfo
from RPG.bot_classes.bot_main_menu import BotMainMenu
from RPG.bot_classes.bot_create_player import BotPlayerCreationMenu
from RPG.bot_classes.create_spaceship import SpaceshipCreationMenu
from RPG.bot_classes.bot_player_profile import BotPlayerProfile
from RPG.bot_classes.locations.main_street import MainStreetLocation
from RPG.bot_classes.locations.ruined_house import RuinedHouseLocation
from RPG.bot_classes.locations.spaceship.spaceship import Spaceship
from RPG.bot_classes.locations.planets.estrad.estrad import Estrad
from RPG.game_classes.player import Player


class BotGame:
    def __init__(self, bot):
        self.players = {}
        self.bot = bot
        self.player_creation_menu = BotPlayerCreationMenu(self)
        self.spaceship_creation_menu = SpaceshipCreationMenu(self)
        self.main_menu = BotMainMenu(self)
        self.inventory = BotInventory(self)
        self.inventory_item_info = BotInventoryItemInfo(self)
        self.player_profile = BotPlayerProfile(self)

        self.main_street_location = {}
        self.ruined_house_location = {}
        self.spaceship = {}
        self.estrad = {}

        self.planets = {}

    def start_new_game(self, command):
        self.players[command.chat.id] = Player(None)

        self.main_street_location[command.chat.id] = MainStreetLocation(self)
        self.ruined_house_location[command.chat.id] = RuinedHouseLocation(self)
        self.spaceship[command.chat.id] = Spaceship(self)
        self.estrad[command.chat.id] = Estrad(self)

        self.planets['эстрад'] = self.estrad

        self.players[command.chat.id].current_location = self.spaceship[command.chat.id].cabin
