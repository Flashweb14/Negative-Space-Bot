from telebot.types import ReplyKeyboardMarkup
from RPG.bot_classes.locations.base_location import BaseLocation
from RPG.game_states import RUINED_HOUSE
from RPG.bot_classes.container import Container
from RPG.game_states import RUINED_HOUSE_BOX
from RPG.game_classes.base_weapon import BaseWeapon


class RuinedHouseLocation(BaseLocation):
    def __init__(self, bot_game):
        super().__init__(bot_game, RUINED_HOUSE, 'Разрушенное здание',
                         'Ты зашёл в старое, занесённое песками, разрушенное здание. В нём ты обнаружил'
                         'старый ржавый ящик. Возможно в нём есть что-то ценное.')
        self.box = Container(bot_game, RUINED_HOUSE_BOX, 'Ты резко дёргаешь проржавевшую крышку ящика, и она, '
                                                         'поддавшись, открывается. Внутри ты находишь старый, '
                                                         'побитый '
                                                         'и перемотанный изолентой лазерный пистолет.',
                             BaseWeapon('Лазерный пистолет', 15, (100, 100), 'Лазерная батарея', 500))

    def show(self, message):
        reply_keyboard = ReplyKeyboardMarkup(True, True)
        reply_keyboard.row('🗃Старый ящик', '⬅️Назад на главную улицу')
        reply_keyboard.row('📟Главное меню')
        self.bot_game.bot.send_message(message.chat.id, self.show_message, parse_mode='Markdown',
                                       reply_markup=reply_keyboard)
        for player_id in self.bot_game.players:
            if player_id != message.chat.id and self.bot_game.players[player_id].state == self.game_state:
                self.bot_game.bot.send_message(player_id, f'Ты видишь как в эти же руины заходит игрок с'
                                                          f' именем {self.bot_game.players[message.chat.id].name}')
                self.bot_game.bot.send_message(message.chat.id, f'Ты видишь как в этих руинах уже находится игрок '
                                                                f'с именем {self.bot_game.players[player_id].name}')

    def handle(self, message):
        if message.text == '🗃Старый ящик':
            self.box.start(message)
        elif message.text == '⬅️Назад на главную улицу':
            self.bot_game.main_street_location[message.chat.id].start(message)
        elif message.text == '📟Главное меню':
            self.bot_game.main_menu.start(message)
