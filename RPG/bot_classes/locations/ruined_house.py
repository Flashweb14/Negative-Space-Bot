from telebot.types import ReplyKeyboardMarkup
from RPG.bot_classes.locations.base_location import BaseLocation
from RPG.game_states import RUINED_HOUSE


class RuinedHouseLocation(BaseLocation):
    def __init__(self, bot_game):
        super().__init__(bot_game, RUINED_HOUSE, 'Разрушенное здание',
                         'Ты зашёл в старое, занесённое песками, разрушенное здание. В нём ты обнаружил'
                         'старый ржавый ящик. Возможно в нём есть что-то ценное.')

    def show(self, message):
        reply_keyboard = ReplyKeyboardMarkup(True, True)
        reply_keyboard.row('🗃Старый ящик', '⬅️Назад на главную улицу')
        reply_keyboard.row('📟Главное меню')
        self.bot_game.bot.send_message(message.chat.id, self.show_message, parse_mode='Markdown',
                                       reply_markup=reply_keyboard)

    def handle(self, message):
        if message.text == '🗃Старый ящик':
            self.bot_game.bot.send_message(message.chat.id, 'Его пока нельзя открыть')
        elif message.text == '⬅️Назад на главную улицу':
            self.bot_game.main_street_location.start(message)
        elif message.text == '📟Главное меню':
            self.bot_game.main_menu.start(message)
