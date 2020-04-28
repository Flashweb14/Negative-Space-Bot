import telebot
from RPG.bot_classes.base_handler import BaseHandler
from RPG.game_states import MAIN_MENU


class MainMenu(BaseHandler):
    def __init__(self, game):
        super().__init__(game, MAIN_MENU)

    def show(self, message):
        main_menu_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        main_menu_keyboard.row('🎒Инвентарь', '⛑Снаряжение')
        main_menu_keyboard.row('📒Журнал', '📟Профиль')
        main_menu_keyboard.row('👀Осмотреться')
        self.game.bot.send_message(message.chat.id, 'Главное меню', reply_markup=main_menu_keyboard)

    def handle(self, message):
        if message.text == '🎒Инвентарь':
            self.game.inventory.start(message)
        elif message.text == '⛑Снаряжение':
            pass
        elif message.text == '📒Журнал':
            pass
        elif message.text == '📟Профиль':
            self.game.player_profile.start(message)
        elif message.text == '👀Осмотреться':
            self.game.players[message.chat.id].current_location.start(message)
        else:
            self.game.bot.send_message(message.chat.id, 'Введено неверное значение')
