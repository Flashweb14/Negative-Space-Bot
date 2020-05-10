from telebot.types import ReplyKeyboardMarkup
from RPG.bot_classes.base_handler import BaseHandler


class Container(BaseHandler):  # Базовый класс дял всех контейнеров
    def __init__(self, game, state, description, item):
        super().__init__(game, state)
        self.description = description
        self.item = item

    def show(self, message):
        if self.item is not None:
            reply_keyboard = ReplyKeyboardMarkup(True, True)
            reply_keyboard.row('✔Взять', '✖Оставить')
            self.game.bot.send_message(message.chat.id, self.description, reply_markup=reply_keyboard)
        else:
            reply_keyboard = ReplyKeyboardMarkup(True, True)
            reply_keyboard.row('⬅Назад')
            self.game.bot.send_message(message.chat.id, 'В ящике пусто', reply_markup=reply_keyboard)

    def handle(self, message):
        if self.item is not None:
            if message.text == '✔Взять':
                self.game.player.add_item(self.item)
                self.item = None
                self.game.current_location.start(message)
            elif message.text == '✖Оставить':
                self.game.current_location.start(message)
            else:
                self.game.bot.send_message(message.chat.id, 'Введено неверное значение')
        else:
            if message.text == '⬅Назад':
                self.game.current_location.start(message)
            else:
                self.game.bot.send_message(message.chat.id, 'Введено неверное значение')
