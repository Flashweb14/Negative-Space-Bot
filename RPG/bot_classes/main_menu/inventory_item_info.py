from telebot.types import ReplyKeyboardMarkup
from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import INVENTORY_INFO
from RPG.game_classes.items.base_weapon import BaseWeapon


class InventoryItemInfo(BaseHandler):
    def __init__(self, game):
        super().__init__(game, INVENTORY_INFO)

    def show(self, call):
        item = self.game.player.inventory[int(call.data)]
        self.game.player.chosen_item = item
        self.reply_keyboard = ReplyKeyboardMarkup(True, True)
        if isinstance(item, BaseWeapon):
            self.reply_keyboard.row('✔Экипировать', '✖Выбросить')
            self.reply_keyboard.row('⬅Назад')
        else:
            self.reply_keyboard.row('✔Использовать', '✖Выбросить')
            self.reply_keyboard.row('⬅Назад')
        self.game.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        self.game.bot.delete_message(call.message.chat.id, call.message.message_id)
        self.game.bot.send_message(call.message.chat.id,
                                   item.get_info(),
                                   parse_mode='Markdown',
                                   reply_markup=self.reply_keyboard)

    def handle(self, message):
        if message.text == '✔Экипировать':
            if isinstance(self.game.player.chosen_item, BaseWeapon):
                self.game.player.equip_weapon(self.game.player.chosen_item)
            else:
                self.show_input_error(message)
            self.game.inventory.start(message)
        elif message.text == '✔Использовать':
            if isinstance(self.game.player.chosen_item, BaseWeapon):
                self.show_input_error(message)
            else:
                self.game.player.chosen_item.use(self.game.player)
            self.game.inventory.start(message)
        elif message.text == '✖Выбросить':
            self.game.player.drop_item(self.game.player.chosen_item)
            self.game.inventory.start(message)
        elif message.text == '⬅Назад':
            self.game.inventory.start(message)
        else:
            self.show_input_error(message)
