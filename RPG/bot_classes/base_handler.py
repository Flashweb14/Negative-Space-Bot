from telebot.types import ReplyKeyboardMarkup


class BaseHandler:  # Базовый обработчик, от него наследуются все классы из bot_classes
    def __init__(self, game, game_state):
        self.game = game
        self.game_state = game_state
        self.reply_keyboard = ReplyKeyboardMarkup(True, True)

    def start(self, message):
        self.game.state = self.game_state
        self.show(message)

    def show(self, message):
        pass

    def handle(self, message):
        pass

    def show_input_error(self, message):
        self.game.bot.send_message(message.chat.id, 'Введена недопустимая команда, попробуй ещё раз.',
                                   reply_markup=self.reply_keyboard)
