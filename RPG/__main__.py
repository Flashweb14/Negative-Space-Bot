import telebot
from RPG.game_classes.game import Game
from RPG.game_classes.base_weapon import BaseWeapon
from RPG.consts import MAIN_MENU, INVENTORY, INVENTORY_INFO, ZERO_STATE, NONE_STATE

bot = telebot.TeleBot('1246120529:AAE8WYmn-o2hlOI-bjUl1BM1akLDYjYzI2o')

games = {}
pistol = BaseWeapon('🔫Лазерный пистолет', 2, (100, 100), 'Лазерная батарея', 200)
riffle = BaseWeapon('🔫Лазерная винтовка', 8, (100, 100), 'Лазерная батарея', 600)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.chat.id in games:
        if games[message.chat.id].state == ZERO_STATE:
            pass
        elif games[message.chat.id].state == MAIN_MENU:
            main_menu_handler(message)
        elif games[message.chat.id].state == INVENTORY_INFO:
            item_info_handler(message)
        elif message.text == '/main_menu':
            show_main_menu(message)
            games[message.chat.id].state = MAIN_MENU
        elif message.text == '/add':
            pistol = BaseWeapon('🔫Лазерный пистолет', 2, (100, 100), 'Лазерная батарея', 200)
            riffle = BaseWeapon('🔫Лазерная винтовка', 8, (100, 100), 'Лазерная батарея', 600)
            games[message.chat.id].player.add_item(pistol)
            games[message.chat.id].player.add_item(riffle)
    elif message.text == '/start':
        start_new_game(message)
        games[message.chat.id].state = NONE_STATE


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if games[call.message.chat.id].state == INVENTORY:
        inventory_handler(call)


def start_new_game(command):
    games[command.chat.id] = Game()


def show_main_menu(message):
    main_menu_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    main_menu_keyboard.row('🎒Инвентарь', '⛑Снаряжение')
    main_menu_keyboard.row('📒Журнал', '📟Профиль')
    bot.send_message(message.chat.id, 'Главное меню', reply_markup=main_menu_keyboard)


def main_menu_handler(message):
    if message.text == '🎒Инвентарь':
        show_inventory(message)
        games[message.chat.id].state = INVENTORY
    elif message.text == '⛑Снаряжение':
        pass
    elif message.text == '📒Журнал':
        pass
    elif message.text == '📟Профиль':
        pass
    else:
        bot.send_message(message.chat.id, 'Введено неверное значение')


def show_inventory(message):
    games[message.chat.id].state = INVENTORY
    inventory_inline_keyboard = telebot.types.InlineKeyboardMarkup()
    for item in games[message.chat.id].player.inventory:
        if item is None:
            btn = telebot.types.InlineKeyboardButton(text='<Пустой слот>',
                                                     callback_data=str(
                                                         games[message.chat.id].player.inventory.index(item)))
        else:
            btn = telebot.types.InlineKeyboardButton(text=str(item),
                                                     callback_data=str(
                                                         games[message.chat.id].player.inventory.index(item)))
        inventory_inline_keyboard.add(btn)
    close_btn = telebot.types.InlineKeyboardButton(text='⬅Назад',
                                                   callback_data='back')
    inventory_inline_keyboard.add(close_btn)
    bot.send_message(message.chat.id, '🎒Инвентарь:', reply_markup=inventory_inline_keyboard)


def inventory_handler(call):
    if call.data == 'back':
        games[call.message.chat.id].state = MAIN_MENU
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        show_main_menu(call.message)
    else:
        show_item_info(call)
        games[call.message.chat.id].state = INVENTORY_INFO


def show_item_info(call):
    item = games[call.message.chat.id].player.inventory[int(call.data)]
    games[call.message.chat.id].chosen_item = item
    if item is not None:
        if item.type == 'weapon':
            item_info = f'*{item.name}* \n' \
                        f'Урон: _{item.damage}_ \n' \
                        f'Прочность: _{item.durability}/{item.max_durability}_ \n' \
                        f'Тип боеприпасов: _{item.ammo_type}_'
            action_keyboard = telebot.types.ReplyKeyboardMarkup(True, True, row_width=2)
            action_keyboard.row('✔Экипировать', '✖Выбросить')
            action_keyboard.row('⬅Назад')
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id,
                             item_info,
                             parse_mode='Markdown',
                             reply_markup=action_keyboard)


def item_info_handler(message):
    if message.text == '✔Экипировать':
        if games[message.chat.id].chosen_item.type == 'weapon':
            games[message.chat.id].player.equip_weapon(games[message.chat.id].chosen_item)
        games[message.chat.id].state = INVENTORY
        show_inventory(message)
    elif message.text == '✖Выбросить':
        games[message.chat.id].player.drop_item(games[message.chat.id].chosen_item)
        games[message.chat.id].state = INVENTORY
        show_inventory(message)
    elif message.text == '⬅Назад':
        games[message.chat.id].state = INVENTORY
        show_inventory(message)


bot.polling()
