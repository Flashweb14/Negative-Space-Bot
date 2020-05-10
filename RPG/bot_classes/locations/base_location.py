from telebot.types import ReplyKeyboardMarkup
from RPG.bot_classes.base_handler import BaseHandler


class BaseLocation(BaseHandler):
    def __init__(self, game, game_state, name, description, enemy=None):
        super().__init__(game, game_state)
        self.name = name
        self.description = description
        self.enemy = enemy
        self.show_message = f'*{self.name}*\n' \
                            f'{self.description}'
        self.reply_keyboard = ReplyKeyboardMarkup(True, True)

    def start(self, message):
        self.game.state = self.game_state
        self.game.current_location = self
        if not self.enemy:
            self.show(message)
        else:
            self.game.fight_system.start_fight(message, self.enemy)

    def show(self, message):
        self.game.bot.send_message(message.chat.id, f'*{self.name}*\n'
                                                    f'{self.description}',
                                   parse_mode='Markdown', reply_markup=self.reply_keyboard)

    def handle(self, message):
        pass
