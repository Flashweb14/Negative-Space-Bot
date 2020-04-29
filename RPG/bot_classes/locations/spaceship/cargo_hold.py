from RPG.consts.game_states import CARGO_HOLD
from RPG.bot_classes.locations.base_location import BaseLocation


class CargoHold(BaseLocation):
    def __init__(self, game, spaceship):
        super().__init__(game, CARGO_HOLD, 'Грузовой отсек', 'Ты заходишь в просторный грузовой отсек. Пока здесь '
                                                                 'пусто. Позже ты сможешь перевозить здесь товары.')
        self.spaceship = spaceship
        self.reply_keyboard.row('🚀Капитанский мостик', '🛏Личная каюта')
        self.reply_keyboard.row('👣Выйти из корабля', '📟Главное меню')

    def handle(self, message):
        if message.text == '🚀Капитанский мостик':
            self.spaceship.captain_bridge.start(message)
        elif message.text == '📟Главное меню':
            self.game.main_menu.start(message)
        elif message.text == '👣Выйти из корабля':
            if not self.game.current_planet:
                self.game.bot.send_message(message.chat.id, 'В открытый космос?0_о Не лучшая идея.',
                                               reply_markup=self.reply_keyboard)
            else:
                self.game.current_planet.start(message)
        elif message.text == '🛏Личная каюта':
            self.spaceship.cabin.start(message)
        else:
            self.show_input_error(message)
