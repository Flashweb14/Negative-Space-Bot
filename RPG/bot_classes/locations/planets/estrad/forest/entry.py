from RPG.bot_classes.locations.base_location import BaseLocation
from RPG.consts.game_states import ESTRAD_FOREST_ENTRY


class ForestEntry(BaseLocation):
    def __init__(self, game):
        super().__init__(game, ESTRAD_FOREST_ENTRY, 'Вход в лес',
                         'Сквозь сырой туман ты подходишь ко входу в густой лес. Перед '
                         'собой ты видишь предупреждающую табличку "_Опасно_" и два пути, '
                         'налево и направо.')
        self.reply_keyboard.row('⬅️Налево', '➡️Направо')
        self.reply_keyboard.row('🏘Назад в колонию', '📟Главное меню')

    def handle(self, message):
        if message.text == '⬅️Налево':
            pass
        elif message.text == '➡️Направо':
            pass
        elif message.text == '🏘Назад в колонию':
            self.game.estrad.colony.start(message)
        elif message.text == '📟Главное меню':
            self.game.main_menu.start(message)
        else:
            self.show_input_error(message)
