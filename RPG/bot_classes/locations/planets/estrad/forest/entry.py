from RPG.bot_classes.locations.base_location import BaseLocation
from RPG.consts.game_states import ESTRAD_FOREST_ENTRY
from RPG.consts.enemies import ESTRAD_NATIVE


class ForestEntry(BaseLocation):
    def __init__(self, game):
        super().__init__(game, ESTRAD_FOREST_ENTRY, 'Вход в лес',
                         'Сквозь сырой туман ты подходишь ко входу в густой лес. Перед '
                         'собой ты видишь предупреждающую табличку "_Опасно! Остерегайтесь местных племён_" и два пути, '
                         'налево и направо.')
        self.reply_keyboard.row('⬅️Налево', '➡️Направо')
        self.reply_keyboard.row('🏘Назад в колонию', '📟Главное меню')

    def handle(self, message):
        if message.text == '⬅️Налево':
            pass
        elif message.text == '➡️Направо':
            self.game.bot.send_message(message.chat.id,
                                       'Ты выбираешь левый путь. Пока ты углубляешься всё дальше в пучины леса, '
                                       'ты всё чаще начинаешь замечать, как заросли, окружающие тебя, переодически '
                                       'странно двигаются...')
            self.game.fight_system.start_fight(message, ESTRAD_NATIVE)
        elif message.text == '🏘Назад в колонию':
            self.game.estrad.colony.start(message)
        elif message.text == '📟Главное меню':
            self.game.main_menu.start(message)
        else:
            self.show_input_error(message)
