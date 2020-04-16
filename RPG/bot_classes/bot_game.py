from RPG.bot_classes.bot_inventory import BotInventory
from RPG.bot_classes.bot_main_menu import BotMainMenu
from RPG.bot_classes.bot_create_player import BotPlayerCreationMenu
from RPG.game_classes.game import Game


class BotGame:
    def __init__(self, bot):
        self.games = {}
        self.bot = bot
        self.player_creation_menu = BotPlayerCreationMenu(self)
        self.main_menu = BotMainMenu(self)
        self.inventory = BotInventory(self)

    def start_new_game(self, command):
        self.games[command.chat.id] = Game(None)
