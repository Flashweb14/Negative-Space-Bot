import telebot
from RPG.bot_classes.bot_base_handler import BotBaseHandler
from RPG.consts import MAIN_MENU, INVENTORY, INVENTORY_INFO


class BotInventory(BotBaseHandler):
    def __init__(self, bot_game):
        super().__init__(bot_game)

    def show(self, message):
        self.bot_game.games[message.chat.id].state = INVENTORY
        inventory_inline_keyboard = telebot.types.InlineKeyboardMarkup()
        for item in self.bot_game.games[message.chat.id].player.inventory:
            if item is None:
                btn = telebot.types.InlineKeyboardButton(text='<Пустой слот>',
                                                         callback_data=str(
                                                             self.bot_game.games[
                                                                 message.chat.id].player.inventory.index(item)))
            else:
                btn = telebot.types.InlineKeyboardButton(text=str(item),
                                                         callback_data=str(
                                                             self.bot_game.games[
                                                                 message.chat.id].player.inventory.index(item)))
            inventory_inline_keyboard.add(btn)
        close_btn = telebot.types.InlineKeyboardButton(text='⬅Назад',
                                                       callback_data='back')
        inventory_inline_keyboard.add(close_btn)
        self.bot_game.bot.send_message(message.chat.id, '🎒Инвентарь:', reply_markup=inventory_inline_keyboard)

    def handler(self, call):
        if call.data == 'back':
            self.bot_game.games[call.message.chat.id].state = MAIN_MENU
            self.bot_game.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            self.bot_game.bot.delete_message(call.message.chat.id, call.message.message_id)
            self.bot_game.main_menu.show(call.message)
        else:
            self.show_item_info(call)
            self.bot_game.games[call.message.chat.id].state = INVENTORY_INFO

    def show_item_info(self, call):
        item = self.bot_game.games[call.message.chat.id].player.inventory[int(call.data)]
        self.bot_game.games[call.message.chat.id].chosen_item = item
        if item is not None:
            if item.type == 'weapon':
                item_info = f'*{item.name}* \n' \
                            f'Урон: _{item.damage}_ \n' \
                            f'Прочность: _{item.durability}/{item.max_durability}_ \n' \
                            f'Тип боеприпасов: _{item.ammo_type}_'
                action_keyboard = telebot.types.ReplyKeyboardMarkup(True, True, row_width=2)
                action_keyboard.row('✔Экипировать', '✖Выбросить')
                action_keyboard.row('⬅Назад')
                self.bot_game.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                self.bot_game.bot.delete_message(call.message.chat.id, call.message.message_id)
                self.bot_game.bot.send_message(call.message.chat.id,
                                               item_info,
                                               parse_mode='Markdown',
                                               reply_markup=action_keyboard)

    def item_info_handler(self, message):
        if message.text == '✔Экипировать':
            if self.bot_game.games[message.chat.id].chosen_item.type == 'weapon':
                self.bot_game.games[message.chat.id].player.equip_weapon(
                    self.bot_game.games[message.chat.id].chosen_item)
            self.bot_game.games[message.chat.id].state = INVENTORY
            self.show(message)
        elif message.text == '✖Выбросить':
            self.bot_game.games[message.chat.id].player.drop_item(self.bot_game.games[message.chat.id].chosen_item)
            self.bot_game.games[message.chat.id].state = INVENTORY
            self.show(message)
        elif message.text == '⬅Назад':
            self.bot_game.games[message.chat.id].state = INVENTORY
            self.show(message)
