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
        self.reply_keyboard.row('👣Выйти из корабля', '📟Главное меню')

    def handle(self, message):
        if message.text == '🚀Капитанский мостик':
            self.spaceship.captain_bridge.start(message)
        elif message.text == '📟Главное меню':
            self.bot_game.main_menu.start(message)
        elif message.text == '👣Выйти из корабля':
            if not self.bot_game.players[message.chat.id].current_planet:
                self.bot_game.bot.send_message(message.chat.id, 'В открытый космос?0_о Не лучшая идея.',
                                               reply_markup=self.reply_keyboard)
            else:
                self.bot_game.planets[self.bot_game.players[message.chat.id].current_planet][message.chat.id].start(
                    message)
        elif message.text == '🛏Личная каюта':
            self.spaceship.cabin.start(message)
        else:
            self.show_input_error(message)
