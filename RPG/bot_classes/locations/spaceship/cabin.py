from telebot.types import ReplyKeyboardMarkup
from RPG.game_states import CABIN
from RPG.bot_classes.locations.base_location import BaseLocation


class Cabin(BaseLocation):
    def __init__(self, game, spaceship):
        super().__init__(game, CABIN, 'Личная каюта', 'Ты находишься в своей личной каюте, здесь находится '
                                                          'бактокамера, в которой ты можешь подлечить свои раны и '
                                                          'восстановить силы, а так же твой личный ящик с вещами. '
                                                          'В небольшом иллюминаторе ты наблюдаешь бескрайние дали '
                                                          'космоса.')
        self.spaceship = spaceship
        self.reply_keyboard.row('🚀Капитанский мостик', '📦Грузовой отсек')
        self.reply_keyboard.row('👣Выйти из корабля', '📟Главное меню')

    def handle(self, message):
        if message.text == '🚀Капитанский мостик':
            self.game.spaceship[message.chat.id].captain_bridge.start(message)
        elif message.text == '📦Грузовой отсек':
            self.spaceship.cargo_hold.start(message)
        elif message.text == '👣Выйти из корабля':
            if not self.game.players[message.chat.id].current_planet:
                self.game.bot.send_message(message.chat.id, 'В открытый космос?0_о Не лучшая идея.',
                                               reply_markup=self.reply_keyboard)
            else:
                self.game.planets[self.game.players[message.chat.id].current_planet][message.chat.id].start(
                    message)
        elif message.text == '📟Главное меню':
            self.game.main_menu.start(message)
        else:
            self.show_input_error(message)
