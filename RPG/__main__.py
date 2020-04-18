import telebot
from RPG.bot_classes.bot_game import BotGame
from RPG.game_states import MAIN_MENU, INVENTORY, INVENTORY_INFO, ZERO_STATE, NONE_STATE, REGISTRATION, PLAYER_PROFILE

bot = telebot.TeleBot('TOKEN')
bot_game = BotGame(bot)


@bot.message_handler(content_types=['text'])
def text_handle(message):
    if message.chat.id in bot_game.players:
        game = bot_game.players[message.chat.id]
        if game.state == ZERO_STATE:
            pass
        elif game.state == REGISTRATION:
            bot_game.player_creation_menu.handle(message)
        elif bot_game.players[message.chat.id].state == MAIN_MENU:
            bot_game.main_menu.handle(message)
        elif game.state == INVENTORY:
            bot.send_message(message.chat.id, 'Не-а, это здесь не работает')
        elif game.state == INVENTORY_INFO:
            bot_game.inventory.item_info_handle(message)
        elif game.state == PLAYER_PROFILE:
            bot_game.player_profile.handle(message)
        elif message.text == '/main_menu':
            bot_game.main_menu.show(message)
            bot_game.players[message.chat.id].state = MAIN_MENU
    elif message.text == '/start':
        bot_game.start_new_game(message)
        bot_game.player_creation_menu.start(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_handle(call):
    if bot_game.players[call.message.chat.id].state == INVENTORY:
        bot_game.inventory.handle(call)


bot.polling()
