from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import MAIN_MENU


class MainMenu(BaseHandler):
    def __init__(self, game):
        super().__init__(game, MAIN_MENU)
        self.reply_keyboard.row('🎒Инвентарь', '⛑Снаряжение')
        self.reply_keyboard.row('📒Журнал', '📟Профиль')
        self.reply_keyboard.row('👀Осмотреться')

    def show(self, message):
        self.game.bot.send_message(message.chat.id, 'Главное меню', reply_markup=self.reply_keyboard)

    def handle(self, message):
        if message.text == '🎒Инвентарь':
            self.game.inventory.start(message)
        elif message.text == '⛑Снаряжение':
            self.game.equipment.start(message)
        elif message.text == '📒Журнал':
            self.game.journal.start(message)
        elif message.text == '📟Профиль':
            self.game.player_profile.start(message)
        elif message.text == '👀Осмотреться':
            self.game.current_location.start(message)
        else:
            self.game.bot.send_message(message.chat.id, 'Введено неверное значение')
