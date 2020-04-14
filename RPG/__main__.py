import telebot
from RPG.game_classes.game import Game
from RPG.game_classes.base_weapon import BaseWeapon
from RPG.consts import MAIN_MENU, INVENTORY, INVENTORY_INFO, ZERO_STATE

bot = telebot.TeleBot('TOKEN')

game = Game()
pistol = BaseWeapon('🔫Лазерный пистолет', 2, (100, 100), 'Лазерная батарея', 200)
riffle = BaseWeapon('🔫Лазерная винтовка', 8, (100, 100), 'Лазерная батарея', 600)
game.player.add_item(pistol)
game.player.add_item(riffle)


@bot.message_handler(commands=['start'])
def start_message(message):
    if game.state == ZERO_STATE:
        game.state = MAIN_MENU
        main_menu_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        main_menu_keyboard.row('🎒Инвентарь', '⛑Снаряжение')
        main_menu_keyboard.row('📒Журнал', '📟Данные')
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=main_menu_keyboard)


@bot.message_handler(commands=['weapon'])
def show_weapon(message):
    bot.send_message(message.chat.id, str(game.player.weapon))


@bot.message_handler(content_types=['text'])
def message_handler(message):
    if game.state == MAIN_MENU:
        if message.text == '🎒Инвентарь':
            show_inventory(message)
    elif game.state == INVENTORY_INFO:
        if message.text == '✔Экипировать':
            if game.chosen_item.type == 'weapon':
                game.player.equip_weapon(game.chosen_item)
            game.state = INVENTORY
            show_inventory(message)
        elif message.text == '✖Выбросить':
            game.player.drop_item(game.chosen_item)
            game.state = INVENTORY
            show_inventory(message)
        elif message.text == '⬅Назад':
            game.state = INVENTORY
            show_inventory(message)


def show_inventory(message):
    game.state = INVENTORY
    inventory_inline_keyboard = telebot.types.InlineKeyboardMarkup()
    for item in game.player.inventory:
        if item is None:
            btn = telebot.types.InlineKeyboardButton(text='<Пустой слот>',
                                                     callback_data=str(game.player.inventory.index(item)))
        else:
            btn = telebot.types.InlineKeyboardButton(text=str(item),
                                                     callback_data=str(game.player.inventory.index(item)))
        inventory_inline_keyboard.add(btn)
    close_btn = telebot.types.InlineKeyboardButton(text='⬅Назад',
                                                   callback_data='back')
    inventory_inline_keyboard.add(close_btn)
    bot.send_message(message.chat.id, '🎒Инвентарь:', reply_markup=inventory_inline_keyboard)


def show_item_info(item_index, chat_id, message_id):
    game.state = INVENTORY_INFO
    item = game.player.inventory[item_index]
    game.chosen_item = item
    if item is not None:
        if item.type == 'weapon':
            item_info = f'*{item.name}* \n' \
                        f'Урон: _{item.damage}_ \n' \
                        f'Прочность: _{item.durability}/{item.max_durability}_ \n' \
                        f'Тип боеприпасов: _{item.ammo_type}_'
            action_keyboard = telebot.types.ReplyKeyboardMarkup(True, True, row_width=2)
            action_keyboard.row('✔Экипировать', '✖Выбросить')
            action_keyboard.row('⬅Назад')
            bot.edit_message_reply_markup(chat_id, message_id)
            bot.delete_message(chat_id, message_id)
            bot.send_message(chat_id,
                             item_info,
                             parse_mode='Markdown',
                             reply_markup=action_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if game.state == INVENTORY:
        if call.data == 'back':
            game.state = ZERO_STATE
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            start_message(call.message)
        else:
            show_item_info(int(call.data), call.message.chat.id, call.message.message_id)


bot.polling()
