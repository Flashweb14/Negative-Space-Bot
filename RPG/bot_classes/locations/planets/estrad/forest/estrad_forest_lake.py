from RPG.bot_classes.locations.base_location import BaseLocation
from RPG.consts.game_states import ESTRAD_FOREST_LAKE


class ForestLake(BaseLocation):
    def __init__(self, game):
        super().__init__(game, ESTRAD_FOREST_LAKE, 'Озеро', 'Ты поворачиваешь налево и долго пробираешься '
                                                            'сквозь густые ветви местной экзотической флоры, '
                                                            'но неожиданно, сделав очередной шаг вперёд, ты'
                                                            ' проваливаешься по колено в воду. Ты понимаешь, что '
                                                            'здесь находится огромное озро, скрытое туманом. Пожалуй, '
                                                            'не стоит проверять, кто может обитать в его водах...')

        self.reply_keyboard.row('⬅️ Назад')

    def handle(self, message):
        if message.text == '⬅️ Назад':
            self.game.estrad.forest.entry.start(message)
        else:
            self.show_input_error(message)
