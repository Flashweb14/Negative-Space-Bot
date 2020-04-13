import telebot
from RPG.game_classes.player import Player
from RPG.game_classes.base_weapon import BaseWeapon

bot = telebot.TeleBot('1246120529:AAHN-l0hZgaw81wlB71DB4IZsYuQoyH6hsE')

player = Player()
pistol = BaseWeapon('🔫Лазерный пистолет', 2, (100, 100), 'battery', 20, 200)
riffle = BaseWeapon('🔫Лазерная винтовка', 8, (100, 100), 'battery', 10, 600)
player.add_item(pistol)
player.add_item(riffle)


@bot.message_handler(commands=['start'])
def start_message(message):
    main_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    main_keyboard.row('🎒Инвентарь')
    bot.send_message(message.chat.id, 'Работа с ботом начата', reply_markup=main_keyboard)


@bot.message_handler(content_types=['text'])
def show_inventory(message):
    inventory_inline_keyboard = telebot.types.InlineKeyboardMarkup()
    if message.text == '🎒Инвентарь':
        for item in player.inventory:
            if item is None:
                btn = telebot.types.InlineKeyboardButton(text='<Пустой слот>',
                                                         callback_data=str(player.inventory.index(item)))
            else:
                btn = telebot.types.InlineKeyboardButton(text=str(item),
                                                         callback_data=str(player.inventory.index(item)))
            inventory_inline_keyboard.add(btn)
        bot.send_message(message.chat.id, '🎒Инвентарь:', reply_markup=inventory_inline_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    print(player.inventory[int(call.data)])


bot.polling()
