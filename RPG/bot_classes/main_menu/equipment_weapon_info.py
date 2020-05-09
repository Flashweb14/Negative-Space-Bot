from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import EQUIPMENT_WEAPON_INFO


class EquipmentWeaponInfo(BaseHandler):
    def __init__(self, game):
        super().__init__(game, EQUIPMENT_WEAPON_INFO)
        self.reply_keyboard.row('⬇️ Снять', '✖️ Выбросить')
        self.reply_keyboard.row('🔄 Перезарядить', '⬅️ Назад')

    def show(self, message):
        self.game.bot.send_message(message.chat.id, f'{self.game.player.weapon.get_info()}',
                                   parse_mode='Markdown', reply_markup=self.reply_keyboard)

    def handle(self, message):
        if message.text == '⬇️ Снять':
            if self.game.player.add_item(self.game.player.weapon):
                self.game.bot.send_message(message.chat.id, f'{self.game.player.weapon.name} успешно снято!')
                self.game.player.weapon = None
            else:
                self.game.bot.send_message(message.chat.id,
                                           f'Не удалось снять {self.game.player.weapon.name}: инвентарь полон!')
            self.game.equipment.start(message)
        elif message.text == '✖️ Выбросить':
            self.game.bot.send_message(message.chat.id, f'{self.game.player.weapon.name} успешно выброшено!')
            self.game.player.weapon = None
            self.game.equipment.start(message)
        elif message.text == '🔄 Перезарядить':
            self.game.bot.send_message(message.chat.id, self.game.player.weapon.reload(self.game.player))
            self.game.equipment.start(message)
        elif message.text == '⬅️ Назад':
            self.game.equipment.start(message)
        else:
            self.show_input_error(message)
