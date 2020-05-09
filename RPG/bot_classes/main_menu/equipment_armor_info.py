from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import EQUIPMENT_ARMOR_INFO


class EquipmentArmorInfo(BaseHandler):
    def __init__(self, game):
        super().__init__(game, EQUIPMENT_ARMOR_INFO)
        self.reply_keyboard.row('⬇️ Снять', '✖️ Выбросить')
        self.reply_keyboard.row('⬅️ Назад')

    def show(self, message):
        self.game.bot.send_message(message.chat.id, f'{self.game.player.armor_set.get_info()}',
                                   parse_mode='Markdown', reply_markup=self.reply_keyboard)

    def handle(self, message):
        if message.text == '⬇️ Снять':
            if self.game.player.add_item(self.game.player.armor_set):
                self.game.bot.send_message(message.chat.id, f'{self.game.player.armor_set.name} успешно снято!')
                self.game.player.armor_set = None
            else:
                self.game.bot.send_message(message.chat.id,
                                           f'Не удалось снять {self.game.player.armor_set.name}: инвентарь полон!')
            self.game.equipment.start(message)
        elif message.text == '✖️ Выбросить':
            self.game.bot.send_message(message.chat.id, f'{self.game.player.armor_set.name} успешно выброшено!')
            self.game.player.armor_set = None
            self.game.equipment.start(message)
        elif message.text == '⬅️ Назад':
            self.game.equipment.start(message)
        else:
            self.show_input_error(message)
