from telebot.types import ReplyKeyboardMarkup
from RPG.game_states import CARGO_HOLD
from RPG.bot_classes.locations.base_location import BaseLocation


class CargoHold(BaseLocation):
    def __init__(self, bot_game, spaceship):
        super().__init__(bot_game, CARGO_HOLD, 'Грузовой отсек', 'Ты заходишь в просторный грузовой отсек. Пока здесь '
                                                                 'пусто. Позже ты сможешь перевозить здесь товары.')
        self.spaceship = spaceship
        self.reply_keyboard = ReplyKeyboardMarkup(True, True)
        self.reply_keyboard.row('🚀Капитанский мостик', '🛏Личная каюта')
        self.reply_keyboard.row('📟Главное меню')

    def handle(self, message):
        if message.text == '🚀Капитанский мостик':
            self.spaceship.captain_bridge.start(message)
        elif message.text == '📟Главное меню':
            self.bot_game.main_menu.start(message)
        elif message.text == '🛏Личная каюта':
            self.spaceship.cabin.start(message)
        else:
            self.show_input_error(message)
