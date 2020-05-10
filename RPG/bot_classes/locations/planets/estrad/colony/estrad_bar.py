from RPG.bot_classes.locations.base_location import BaseLocation
from RPG.consts.game_states import ESTRAD_BAR


class EstradBar(BaseLocation):
    def __init__(self, game):
        super().__init__(game, ESTRAD_BAR, 'Бар "Гарцующий брамин"', 'Ты заходишь в бар. За барной стойкой сидят '
                                                                     'несколько солдат федерации. Сейчас здесь '
                                                                     'не происходит ничего интересного...')
        self.reply_keyboard.row('⬅️ Назад')

    def handle(self, message):
        if message.text == '⬅️ Назад':
            self.game.estrad.colony.start(message)
        else:
            self.show_input_error(message)
