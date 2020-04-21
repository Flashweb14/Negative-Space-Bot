from telebot.types import ReplyKeyboardMarkup
from RPG.bot_classes.locations.base_location import BaseLocation
from RPG.game_states import MAIN_STREET


class MainStreetLocation(BaseLocation):
    def __init__(self, bot_game):
        super().__init__(bot_game, MAIN_STREET, 'Небольшое поселение',
                         'Ты находишься на главной улице небольшого поселения, затярянного в песках этой планеты.'
                         'Перед собой ты видишь небольшую лавчонку, построенную из листов ржавого железа и'
                         'старой техники, а так же руины какого-то здания.')

    def show(self, message):
        reply_keyboard = ReplyKeyboardMarkup(True, True)
        reply_keyboard.row('👳🏾‍♂️Торговец', '🏚Руины')
        reply_keyboard.row('📟Главное меню')
        self.bot_game.bot.send_message(message.chat.id, self.show_message, parse_mode='Markdown',
                                       reply_markup=reply_keyboard)
        for player_id in self.bot_game.players:
            if player_id != message.chat.id and self.bot_game.players[player_id].state == self.game_state:
                self.bot_game.bot.send_message(player_id, f'Ты видишь как на эту же главную улицу заходит игрок с'
                                                          f' именем {self.bot_game.players[player_id].name}')
                self.bot_game.bot.send_message(message.chat.id, f'Ты видишь как на этой же улице уже находится игрок '
                                                                f'с именем {self.bot_game.players[player_id].name}')

    def handle(self, message):
        if message.text == '👳🏾‍♂️Торговец':
            self.bot_game.bot.send_message(message.chat.id, 'К нему пока нельзя')
        elif message.text == '🏚Руины':
            self.bot_game.ruined_house_location[message.chat.id].start(message)
        elif message.text == '📟Главное меню':
            self.bot_game.main_menu.start(message)
