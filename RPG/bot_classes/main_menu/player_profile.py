from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import PLAYER_PROFILE


class PlayerProfile(BaseHandler):
    def __init__(self, game):
        super().__init__(game, PLAYER_PROFILE)
        self.reply_keyboard.row('⬅Назад')

    def show(self, message):
        player = self.game.player
        player_profile = f'*{player.name}*😎\n' \
                         f'🎖_Уровень_: {player.level}\n' \
                         f'❤️_Здоровье_: {player.hp}\n' \
                         f'💵_Кредиты_: {player.money}\n' \
                         f'*Характеристики*\n' \
                         f'💪🏻_Сила_: {player.strength}\n' \
                         f'👂🏻_Восприятие_: {player.perception}\n' \
                         f'🏃🏻‍♂️_Выносливость_: {player.endurance}\n' \
                         f'🗣_Харизма_: {player.charisma}\n' \
                         f'🧠_Интеллект_: {player.intelligence}\n' \
                         f'🤸🏻‍♂️_Ловкость_: {player.agility}\n' \
                         f'🍀_Удача_: {player.luck}'
        self.game.bot.send_message(message.chat.id, player_profile, parse_mode='Markdown',
                                   reply_markup=self.reply_keyboard)

    def handle(self, message):
        if message.text == '⬅Назад':
            self.game.main_menu.start(message)
        else:
            self.game.bot.send_message(message.chat.id, 'Туты так низзя')
