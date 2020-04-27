import telebot
from RPG.bot_classes.bot_game import BotGame
from RPG.game_states import MAIN_MENU, INVENTORY, INVENTORY_INFO, ZERO_STATE, NONE_STATE, REGISTRATION, PLAYER_PROFILE, \
    CABIN, CAPTAIN_BRIDGE, CARGO_HOLD, COMPUTER, CREATE_SPACESHIP, ESTRAD_PORT, ESTRAD_SECURITY_SOLDIER

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
        elif game.state == CREATE_SPACESHIP:
            bot_game.spaceship_creation_menu.handle(message)
        elif bot_game.players[message.chat.id].state == MAIN_MENU:
            bot_game.main_menu.handle(message)
        elif game.state == INVENTORY:
            bot.send_message(message.chat.id, 'Не-а, это здесь не работает')
        elif game.state == INVENTORY_INFO:
            bot_game.inventory_item_info.handle(message)
        elif game.state == PLAYER_PROFILE:
            bot_game.player_profile.handle(message)
        elif game.state == CABIN:
            bot_game.spaceship[message.chat.id].cabin.handle(message)
        elif game.state == CAPTAIN_BRIDGE:
            bot_game.spaceship[message.chat.id].captain_bridge.handle(message)
        elif game.state == CARGO_HOLD:
            bot_game.spaceship[message.chat.id].cargo_hold.handle(message)
        elif game.state == COMPUTER:
            bot_game.spaceship[message.chat.id].computer.handle(message)
        elif game.state == ESTRAD_PORT:
            bot_game.estrad[message.chat.id].port.handle(message)
        elif game.state == ESTRAD_SECURITY_SOLDIER:
            bot_game.estrad[message.chat.id].security_soldier.handle(message)
        elif message.text == '/main_menu':
            bot_game.main_menu.show(message)
            bot_game.players[message.chat.id].state = MAIN_MENU
    elif message.text == '/start':
        bot_game.start_new_game(message)
        bot_game.player_creation_menu.start(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_handle(call):
    game = bot_game.players[call.message.chat.id]
    if game.state == INVENTORY:
        bot_game.inventory.handle(call)


bot.polling()
