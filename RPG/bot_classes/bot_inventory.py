import telebot
from RPG.bot_classes.bot_base_handler import BotBaseHandler
from RPG.game_states import INVENTORY


class BotInventory(BotBaseHandler):
    def __init__(self, bot_game):
        super().__init__(bot_game, INVENTORY)

    def show(self, message):
        inventory_inline_keyboard = telebot.types.InlineKeyboardMarkup()
        for item in self.bot_game.players[message.chat.id].inventory:
            if item is None:
                btn = telebot.types.InlineKeyboardButton(text='<Пустой слот>',
                                                         callback_data=str(
                                                             self.bot_game.players[
                                                                 message.chat.id].inventory.index(item)))
            else:
                btn = telebot.types.InlineKeyboardButton(text=str(item),
                                                         callback_data=str(
                                                             self.bot_game.players[
                                                                 message.chat.id].inventory.index(item)))
            inventory_inline_keyboard.add(btn)
        close_btn = telebot.types.InlineKeyboardButton(text='⬅Назад',
                                                       callback_data='back')
        inventory_inline_keyboard.add(close_btn)
        self.bot_game.bot.send_message(message.chat.id, '🎒Инвентарь:', reply_markup=inventory_inline_keyboard)

    def handle(self, call):
        if call.data == 'back':
            self.bot_game.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            self.bot_game.bot.delete_message(call.message.chat.id, call.message.message_id)
            self.bot_game.main_menu.start(call.message)
        else:
            self.bot_game.invetory_item_info(call.message)
