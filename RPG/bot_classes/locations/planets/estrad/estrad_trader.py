from RPG.consts.game_states import ESTRAD_TRADER
from RPG.bot_classes.base_dialog import BaseDialog


class EstradTrader(BaseDialog):
    def __init__(self, game):
        super().__init__(game, ESTRAD_TRADER, 'Солдат Межгалактической Республики', 'Здравия желаю! Здесь '
                                                                                    'ты можешь получить базовый '
                                                                                    'комплект солдата федерации, если у'
                                                                                    ' тебя есть удостоверение, или '
                                                                                    'купить дополнительное снаряжение,'
                                                                                    ' если базового тебе недостаточно.',
                         '👨🏼')
        self.reply_keyboard.row('Покажи мне свои товары.')
        self.reply_keyboard.row('Хочу получить комплект.')
        self.reply_keyboard.row('Мне уже пора.')

    def handle(self, message):
        if message.text == 'Покажи мне свои товары.':
            pass
        elif message.text == 'Хочу получить комплект.':
            pass
        elif message.text == 'Мне уже пора.':
            self.say(message, 'Заходи ещё.')
            self.game.planets.estrad.colony.start(message)
        else:
            self.show_input_error(message)
