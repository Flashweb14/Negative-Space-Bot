from telebot.types import ReplyKeyboardMarkup
from RPG.bot_classes.bot_base_handler import BotBaseHandler


class BaseDialog(BotBaseHandler):
    def __init__(self, bot_game, game_state, name, text, emoji):
        super().__init__(bot_game, game_state)
        self.name = name
        self.text = text
        self.emoji = emoji
        self.show_message = f'{self.emoji}*{self.name}*\n- {self.text}'
        self.reply_keyboard = ReplyKeyboardMarkup(True, True)

    def start(self, message):
        self.bot_game.players[message.chat.id].state = self.game_state
        self.show(message)

    def show_input_error(self, message):
        self.bot_game.bot.send_message(message.chat.id, 'Что? Я тебя не понимаю.',
                                       reply_markup=self.reply_keyboard)

    def say(self, message, text):
        self.bot_game.bot.send_message(message.chat.id, f'{self.emoji}*{self.name}*\n'
                                                        f'{text}',
                                       parse_mode='Markdown', reply_markup=self.reply_keyboard)

    def show(self, message):
        self.bot_game.bot.send_message(message.chat.id, self.show_message,
                                       parse_mode='Markdown', reply_markup=self.reply_keyboard)

    def handle(self, message):
        pass
