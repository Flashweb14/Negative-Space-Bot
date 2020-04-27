from telebot.types import ReplyKeyboardMarkup
from RPG.bot_classes.bot_base_handler import BotBaseHandler


class BaseLocation(BotBaseHandler):
    def __init__(self, bot_game, game_state, name, description):
        super().__init__(bot_game, game_state)
        self.name = name
        self.description = description
        self.show_message = f'*{self.name}*\n' \
                            f'{self.description}'
        self.reply_keyboard = ReplyKeyboardMarkup(True, True)

    def start(self, message):
        self.bot_game.players[message.chat.id].state = self.game_state
        self.bot_game.players[message.chat.id].current_location = self
        self.show(message)

    def show_input_error(self, message):
        self.bot_game.bot.send_message(message.chat.id, 'Введена недопустимая команда, попробуй ещё раз.',
                                       reply_markup=self.reply_keyboard)

    def show(self, message):
        self.bot_game.bot.send_message(message.chat.id, f'*{self.name}*\n'
                                                        f'{self.description}',
                                       parse_mode='Markdown', reply_markup=self.reply_keyboard)

    def handle(self, message):
        pass
