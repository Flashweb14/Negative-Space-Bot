from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import FIGHT_SYSTEM


class FightSystem(BaseHandler):
    def __init__(self, game):
        super().__init__(game, FIGHT_SYSTEM)
        self.enemy = None

    def start_fight(self, message, enemy):
        self.enemy.show_fight_message(message)
        self.game.bot.send_message(message.chat.id, f'⚔️Ты вступил в бой с {enemy.name}⚔️')