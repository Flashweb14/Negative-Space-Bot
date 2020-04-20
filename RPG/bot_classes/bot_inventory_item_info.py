import telebot
from RPG.bot_classes.bot_base_handler import BotBaseHandler
from RPG.game_states import INVENTORY_INFO


class BotInventoryItemInfo(BotBaseHandler):
    def __init__(self, bot_game):
        super().__init__(bot_game, INVENTORY_INFO)

    def start(self, call):
        self.bot_game.players[call.message.chat.id].state = self.game_state
        self.show(call)

    def show(self, call):
        item = self.bot_game.players[call.message.chat.id].inventory[int(call.data)]
        self.bot_game.players[call.message.chat.id].chosen_item = item
        if item is not None:
            if item.type == 'weapon':
                item_info = f'*{item.name}* \n' \
                            f'_🗡Урон_: {item.damage} \n' \
                            f'_🛠Прочность_: {item.durability}/{item.max_durability} \n' \
                            f'_🔋Тип боеприпасов_: {item.ammo_type}'
                action_keyboard = telebot.types.ReplyKeyboardMarkup(True, True, row_width=2)
                action_keyboard.row('✔Экипировать', '✖Выбросить')
                action_keyboard.row('⬅Назад')
                self.bot_game.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                self.bot_game.bot.delete_message(call.message.chat.id, call.message.message_id)
                self.bot_game.bot.send_message(call.message.chat.id,
                                               item_info,
                                               parse_mode='Markdown',
                                               reply_markup=action_keyboard)

    def handle(self, message):
        if message.text == '✔Экипировать':
            if self.bot_game.players[message.chat.id].chosen_item.type == 'weapon':
                self.bot_game.players[message.chat.id].equip_weapon(
                    self.bot_game.players[message.chat.id].chosen_item)
            self.bot_game.inventory.start(message)
        elif message.text == '✖Выбросить':
            self.bot_game.players[message.chat.id].drop_item(self.bot_game.players[message.chat.id].chosen_item)
            self.bot_game.inventory.start(message)
        elif message.text == '⬅Назад':
            self.bot_game.inventory.start(message)
