import telebot
from RPG.game_classes.game import Game
from RPG.game_classes.base_weapon import BaseWeapon

bot = telebot.TeleBot('TOKEN')

game = Game()
pistol = BaseWeapon('🔫Лазерный пистолет', 2, (100, 100), 'Лазерная батарея', 200)
riffle = BaseWeapon('🔫Лазерная винтовка', 8, (100, 100), 'Лазерная батарея', 600)
game.player.add_item(pistol)
game.player.add_item(riffle)


@bot.message_handler(commands=['start'])
def start_message(message):
    main_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    main_keyboard.row('🎒Инвентарь')
    bot.send_message(message.chat.id, 'Работа с ботом начата', reply_markup=main_keyboard)


@bot.message_handler(commands=['weapon'])
def show_weapon(message):
    bot.send_message(message.chat.id, str(game.player.weapon))


@bot.message_handler(content_types=['text'])
def message_handler(message):
    if message.text == '🎒Инвентарь':
        game.inventory_opened = True
        inventory_inline_keyboard = telebot.types.InlineKeyboardMarkup()
        for item in game.player.inventory:
            if item is None:
                btn = telebot.types.InlineKeyboardButton(text='<Пустой слот>',
                                                         callback_data=str(game.player.inventory.index(item)))
            else:
                btn = telebot.types.InlineKeyboardButton(text=str(item),
                                                         callback_data=str(game.player.inventory.index(item)))
            inventory_inline_keyboard.add(btn)
        close_btn = telebot.types.InlineKeyboardButton(text='Назад',
                                                       callback_data='back')
        inventory_inline_keyboard.add(close_btn)
        bot.send_message(message.chat.id, '🎒Инвентарь:', reply_markup=inventory_inline_keyboard)
    elif message.text == '✔Экипировать':
        if game.chosen_item.type == 'weapon':
            game.player.equip_weapon(game.chosen_item)
    elif message.text == '✖Выбросить':
        game.player.drop_item(game.chosen_item)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if game.inventory_opened:
        if call.data == 'back':
            game.inventory_opened = False
        else:
            item = game.player.inventory[int(call.data)]
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
                    bot.send_message(call.message.chat.id,
                                     item_info,
                                     parse_mode='Markdown',
                                     reply_markup=action_keyboard)


bot.polling()
