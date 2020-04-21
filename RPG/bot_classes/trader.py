from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from RPG.bot_classes.bot_base_handler import BotBaseHandler


class Trader(BotBaseHandler):
    def __init__(self, game_bot, game_state, stock_products, products):
        super().__init__(game_bot, game_state)
        self.stock_products = stock_products
        self.products = products

    def show(self, message):
        trader_inline_keyboard = InlineKeyboardMarkup()
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