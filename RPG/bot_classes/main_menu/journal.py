from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import JOURNAL


class Journal(BaseHandler):
    def __init__(self, game):
        super().__init__(game, JOURNAL)
        self.reply_keyboard.row('⬅ Назад')

    def show(self, message):
        self.game.bot.send_message(message.chat.id, f'📒 *Задания*\n'
                                                    f'_У тебя пока нет ни одного задания_(что не удивительно, их '
                                                    f'ещё нельзя получать)', parse_mode='Markdown',
                                   reply_markup=self.reply_keyboard)

    def handle(self, message):
        if message.text == '⬅ Назад':
            self.game.main_menu.start(message)
        else:
            self.show_input_error(message)
