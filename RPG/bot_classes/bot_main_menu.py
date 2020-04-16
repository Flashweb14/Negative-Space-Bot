import telebot
from RPG.bot_classes.bot_base_handler import BotBaseHandler
from RPG.consts import INVENTORY, PLAYER_PROFILE


class BotMainMenu(BotBaseHandler):
    def __init__(self, bot_game):
        super().__init__(bot_game)

    def show(self, message):
        main_menu_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        main_menu_keyboard.row('🎒Инвентарь', '⛑Снаряжение')
        main_menu_keyboard.row('📒Журнал', '📟Профиль')
        self.bot_game.bot.send_message(message.chat.id, 'Главное меню', reply_markup=main_menu_keyboard)

    def handler(self, message):
        if message.text == '🎒Инвентарь':
            self.bot_game.inventory.show(message)
            self.bot_game.games[message.chat.id].state = INVENTORY
        elif message.text == '⛑Снаряжение':
            pass
        elif message.text == '📒Журнал':
            pass
        elif message.text == '📟Профиль':
            self.bot_game.player_profile.show(message)
            self.bot_game.games[message.chat.id].state = PLAYER_PROFILE
        else:
            self.bot_game.bot.send_message(message.chat.id, 'Введено неверное значение')
