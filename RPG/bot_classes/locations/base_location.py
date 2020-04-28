from telebot.types import ReplyKeyboardMarkup
from RPG.bot_classes.base_handler import BaseHandler


class BaseLocation(BaseHandler):
    def __init__(self, game, game_state, name, description):
        super().__init__(game, game_state)
        self.name = name
        self.description = description
        self.show_message = f'*{self.name}*\n' \
                            f'{self.description}'
        self.reply_keyboard = ReplyKeyboardMarkup(True, True)

    def start(self, message):
        self.game.players[message.chat.id].state = self.game_state
        self.game.players[message.chat.id].current_location = self
        self.show(message)

    def show_input_error(self, message):
        self.game.bot.send_message(message.chat.id, 'Введена недопустимая команда, попробуй ещё раз.',
                                       reply_markup=self.reply_keyboard)

    def show(self, message):
        self.game.bot.send_message(message.chat.id, f'*{self.name}*\n'
                                                        f'{self.description}',
                                       parse_mode='Markdown', reply_markup=self.reply_keyboard)

    def handle(self, message):
        pass
