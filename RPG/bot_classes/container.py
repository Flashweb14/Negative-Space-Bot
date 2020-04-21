from telebot.types import ReplyKeyboardMarkup
from RPG.bot_classes.bot_base_handler import BotBaseHandler


class Container(BotBaseHandler):
    def __init__(self, bot_game, state, description, item):
        super().__init__(bot_game, state)
        self.description = description
        self.item = item

    def show(self, message):
        if self.item is not None:
            reply_keyboard = ReplyKeyboardMarkup(True, True)
            reply_keyboard.row('✔Взять', '✖Оставить')
            self.bot_game.bot.send_message(message.chat.id, self.description, reply_markup=reply_keyboard)
        else:
            reply_keyboard = ReplyKeyboardMarkup(True, True)
            reply_keyboard.row('⬅Назад')
            self.bot_game.bot.send_message(message.chat.id, 'В ящике пусто', reply_markup=reply_keyboard)

    def handle(self, message):
        if self.item is not None:
            if message.text == '✔Взять':
                self.bot_game.players[message.chat.id].add_item(self.item)
                self.item = None
                self.bot_game.players[message.chat.id].current_location.start(message)
            elif message.text == '✖Оставить':
                self.bot_game.players[message.chat.id].current_location.start(message)
            else:
                self.bot_game.bot.send_message(message.chat.id, 'Введено неверное значение')
        else:
            if message.text == '⬅Назад':
                self.bot_game.players[message.chat.id].current_location.start(message)
            else:
                self.bot_game.bot.send_message(message.chat.id, 'Введено неверное значение')
