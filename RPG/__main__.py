import telebot
from RPG.game_classes.base_weapon import BaseWeapon
from RPG.bot_classes.bot_game import BotGame
from RPG.consts import MAIN_MENU, INVENTORY, INVENTORY_INFO, ZERO_STATE, NONE_STATE

bot = telebot.TeleBot('1246120529:AAE8WYmn-o2hlOI-bjUl1BM1akLDYjYzI2o')
bot_game = BotGame(bot)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.chat.id in bot_game.games:
        if bot_game.games[message.chat.id].state == ZERO_STATE:
            pass
        elif bot_game.games[message.chat.id].state == MAIN_MENU:
            bot_game.main_menu.handler(message)
        elif bot_game.games[message.chat.id].state == INVENTORY_INFO:
            bot_game.inventory.item_info_handler(message)
        elif message.text == '/main_menu':
            bot_game.main_menu.show(message)
            bot_game.games[message.chat.id].state = MAIN_MENU
        elif message.text == '/add':
            pistol = BaseWeapon('🔫Лазерный пистолет', 2, (100, 100), 'Лазерная батарея', 200)
            riffle = BaseWeapon('🔫Лазерная винтовка', 8, (100, 100), 'Лазерная батарея', 600)
            bot_game.games[message.chat.id].player.add_item(pistol)
            bot_game.games[message.chat.id].player.add_item(riffle)
    elif message.text == '/start':
        bot_game.start_new_game(message)
        bot_game.games[message.chat.id].state = NONE_STATE


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if bot_game.games[call.message.chat.id].state == INVENTORY:
        bot_game.inventory.handler(call)


bot.polling()
