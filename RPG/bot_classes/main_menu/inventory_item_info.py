from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import INVENTORY_INFO


class InventoryItemInfo(BaseHandler):
    def __init__(self, game):
        super().__init__(game, INVENTORY_INFO)
        self.reply_keyboard.row('✔Экипировать', '✖Выбросить')
        self.reply_keyboard.row('⬅Назад')

    def start(self, call):
        self.game.players[call.message.chat.id].state = self.game_state
        self.show(call)

    def show(self, call):
        item = self.game.players[call.message.chat.id].inventory[int(call.data)]
        self.game.players[call.message.chat.id].chosen_item = item
        if item is not None:
            if item.type == 'weapon':
                item_info = f'*{item.name}* \n' \
                            f'_🗡Урон_: {item.damage} \n' \
                            f'_🛠Прочность_: {item.durability}/100 \n' \
                            f'_🔋Тип боеприпасов_: {item.ammo_type}'
                self.game.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                self.game.bot.delete_message(call.message.chat.id, call.message.message_id)
                self.game.bot.send_message(call.message.chat.id,
                                           item_info,
                                           parse_mode='Markdown',
                                           reply_markup=self.reply_keyboard)

    def handle(self, message):
        if message.text == '✔Экипировать':
            if self.game.player.chosen_item.type == 'weapon':
                self.game.player.equip_weapon(
                    self.game.player.chosen_item)
            self.game.inventory.start(message)
        elif message.text == '✖Выбросить':
            self.game.player.drop_item(self.game.player.chosen_item)
            self.game.inventory.start(message)
        elif message.text == '⬅Назад':
            self.game.inventory.start(message)
