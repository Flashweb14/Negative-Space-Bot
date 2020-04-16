import telebot
from RPG.bot_classes.bot_base_handler import BotBaseHandler
from RPG.consts import MAIN_MENU


class BotPlayerProfile(BotBaseHandler):
    def __init__(self, bot_game):
        super().__init__(bot_game)

    def show(self, message):
        player = self.bot_game.games[message.chat.id].player
        player_profile = f'*{player.name}*😎\n' \
                         f'_Уровень_: {player.level}\n' \
                         f'_Здоровье_: {player.hp}\n' \
                         f'*Характеристики*\n' \
                         f'💪🏻_Сила_: {player.strength}\n' \
                         f'👂🏻_Восприятие_: {player.perception}\n' \
                         f'🏃🏻‍♂️_Выносливость_: {player.endurance}\n' \
                         f'🗣_Харизма_: {player.charisma}\n' \
                         f'🧠_Интеллект_: {player.intelligence}\n' \
                         f'🤸🏻‍♂️_Ловкость_: {player.agility}\n' \
                         f'🍀_Удача_: {player.luck}'
        profile_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        profile_keyboard.row('⬅Назад')
        self.bot_game.bot.send_message(message.chat.id, player_profile, parse_mode='Markdown',
                                       reply_markup=profile_keyboard)

    def handler(self, message):
        if message.text == '⬅Назад':
            self.bot_game.games[message.chat.id].state = MAIN_MENU
            self.bot_game.main_menu.show(message)
        else:
            self.bot_game.bot.send_message(message.chat.it, 'Туты так низзя')
