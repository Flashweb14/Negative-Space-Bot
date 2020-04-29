from RPG.consts.game_states import ESTRAD_SECURITY_SOLDIER
from RPG.consts.quest_items import FEDERATION_PASS
from RPG.bot_classes.base_dialog import BaseDialog


class EstradSecuritySoldier(BaseDialog):
    def __init__(self, game, player):
        super().__init__(game, ESTRAD_SECURITY_SOLDIER, 'Солдат Межгалактической Республики',
                         'Приветсвую вас на планете Эстрад, в колонии Межгалактической Республики. Предъявите, '
                         'пожалуйста, ваш пропуск.', '👮🏻‍♂️')
        self.player = player
        self.reply_keyboard.row(
            f'[🗣Харизма {self.player.charisma}/4] Меня прислало высшее руководство передать срочное послание '
            'вашему начальству.')
        self.reply_keyboard.row('[💵250] Может можно как-то договориться?')
        if FEDERATION_PASS in self.player.quest_items:
            self.reply_keyboard.row('Показать пропуск')
        self.reply_keyboard.row('Мне уже пора')

    def handle(self, message):
        if (message.text ==
                f'[🗣Харизма {self.player.charisma}/4] Меня прислало высшее руководство передать срочное послание '
                f'вашему начальству.'):
            if self.game.player.charisma >= 4:
                self.say(message, 'Хорошо, проходи.')
                self.game.estrad.colony.start(message)
            else:
                self.say(message, 'Кого ты пытаешься обмануть? Меня бы предупредили, если'
                                  ' бы начальство кого-то ожидало.')
        elif message.text == '[💵250] Может можно как-то договориться?':
            if self.game.player.money >= 250:
                self.game.player.money -= 250
                self.say(message, 'Хорошо, проходи.')
                self.game.estrad.colony.start(message)
            else:
                self.say(message, 'У тебя и денег то таких нет.')
        elif message.text == 'Мне уже пора':
            self.say(message, 'До встречи.')
            self.estrad.port.start(message)
        else:
            self.show_input_error(message)
