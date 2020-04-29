from RPG.consts.game_states import ESTRAD_COLONY
from RPG.bot_classes.locations.base_location import BaseLocation
from RPG.bot_classes.locations.planets.estrad.estrad_trader import EstradTrader


class EstradColony(BaseLocation):
    def __init__(self, game):
        super().__init__(game, ESTRAD_COLONY, 'Колония', 'Ты заходишь в небольшой военный лагерь. Судя по всему, '
                                                         'колонизаторы прибыли сюда недавно, установка временных '
                                                         'жилых модулей ещё не закончена, и повсюду снуют солдаты '
                                                         'республики, представители разных рас. Ты видишь перед '
                                                         'собой местный бар, пункт выдачи снаряжения'
                                                         ', штаб начальства и дорогу в густой туманный лес.')
        self.reply_keyboard.row('🍻Бар', '🏪Пункт выдачи снаряжения')
        self.reply_keyboard.row('🏕Штаб начальства', '🌲Лес')
        self.reply_keyboard.row('🚀Назад на корабль', '📟Главное меню')

        self.trader = EstradTrader(game)

    def handle(self, message):
        if message.text == '🍻Бар':
            pass
        elif message.text == '🏪Пункт выдачи снаряжения':
            self.trader.start(message)
        elif message.text == '🏕Штаб начальства':
            pass
        elif message.text == '🌲Лес':
            pass
        elif message.text == '🚀Назад на корабль':
            self.game.spaceship.cabin.start(message)
        elif message.text == '📟Главное меню':
            self.game.main_menu.start(message)
        else:
            self.show_input_error(message)
