from RPG.bot_classes.locations.planets.estrad.colony.estrad_bar import EstradBar
from RPG.consts.game_states import ESTRAD_COLONY
from RPG.bot_classes.locations.base_location import BaseLocation
from RPG.bot_classes.locations.planets.estrad.colony.estrad_trader import EstradTrader
from RPG.consts.quest_items import FEDERATION_PASS


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
        self.bar = EstradBar(game)

        self.child_locations = [self.bar]

    def handle(self, message):
        if message.text == '🍻Бар':
            self.bar.start(message)
        elif message.text == '🏪Пункт выдачи снаряжения':
            self.trader.start(message)
        elif message.text == '🏕Штаб начальства':
            if FEDERATION_PASS in self.game.player.quest_items:
                self.game.bot.send_message(message.chat.id, 'У тебя уже есть пропуск, тебе незачем туда идти.')
                self.start(message)
            else:
                self.game.player.quest_items.append(FEDERATION_PASS)
                self.game.bot.send_message(message.chat.id, 'Начальство колонии посвятило тебя в ряды колонизаторов '
                                                            'планеты. Теперь у тебя есть пропуск солдата '
                                                            'федерации.')
                self.start(message)
        elif message.text == '🌲Лес':
            self.game.estrad.forest.entry.start(message)
        elif message.text == '🚀Назад на корабль':
            self.game.spaceship.cabin.start(message)
        elif message.text == '📟Главное меню':
            self.game.main_menu.start(message)
        else:
            self.show_input_error(message)
