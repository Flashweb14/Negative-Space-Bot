from RPG.bot_classes.locations.base_location import BaseLocation
from RPG.consts.enemies import ESTRAD_NATIVE
from RPG.consts.game_states import ESTRAD_FOREST_FIELD


class ForestField(BaseLocation):
    def __init__(self, game):
        super().__init__(game, ESTRAD_FOREST_FIELD, 'Туманная поляна',
                         'Ты выходишь на окутанную густой мглой небольшую поляну. Видимо, '
                         'здесь нет ничего интересного.', ESTRAD_NATIVE)
        self.reply_keyboard.row('⬅️ Назад')
        self.enemy = ESTRAD_NATIVE

    def handle(self, message):
        if message.text == '⬅️ Назад':
            self.game.estrad.forest.entry.start(message)
        else:
            self.show_input_error(message)
