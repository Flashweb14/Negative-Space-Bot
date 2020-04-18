from RPG.bot_classes.bot_inventory import BotInventory
from RPG.bot_classes.bot_inventory_item_info import BotInventoryItemInfo
from RPG.bot_classes.bot_main_menu import BotMainMenu
from RPG.bot_classes.bot_create_player import BotPlayerCreationMenu
from RPG.bot_classes.bot_player_profile import BotPlayerProfile
from RPG.game_classes.player import Player


class BotGame:
    def __init__(self, bot):
        self.players = {}
        self.bot = bot
        self.player_creation_menu = BotPlayerCreationMenu(self)
        self.main_menu = BotMainMenu(self)
        self.inventory = BotInventory(self)
        self.inventory_item_info = BotInventoryItemInfo(self)
        self.player_profile = BotPlayerProfile(self)

    def start_new_game(self, command):
        self.players[command.chat.id] = Player(None)
