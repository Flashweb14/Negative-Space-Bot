import telebot
from RPG.bot_classes.game import Game
from RPG.consts.game_states import MAIN_MENU, INVENTORY, INVENTORY_INFO, REGISTRATION, PLAYER_PROFILE, \
    CABIN, CAPTAIN_BRIDGE, CARGO_HOLD, COMPUTER, CREATE_SPACESHIP, ESTRAD_PORT, ESTRAD_SECURITY_SOLDIER, ESTRAD_COLONY, \
    ESTRAD_TRADER

bot = telebot.TeleBot('TOKEN')
games = {}


@bot.message_handler(content_types=['text'])
def text_handle(message):
    if message.chat.id in games:
        game = games[message.chat.id]
        if game.state == REGISTRATION:
            game.player_creation_menu.handle(message)
        elif game.state == CREATE_SPACESHIP:
            game.spaceship_creation_menu.handle(message)
        elif game.state == MAIN_MENU:
            game.main_menu.handle(message)
        elif game.state == INVENTORY:
            bot.send_message(message.chat.id, 'Не-а, это здесь не работает')
        elif game.state == INVENTORY_INFO:
            game.inventory_item_info.handle(message)
        elif game.state == PLAYER_PROFILE:
            game.player_profile.handle(message)
        elif game.state == CABIN:
            game.spaceship.cabin.handle(message)
        elif game.state == CAPTAIN_BRIDGE:
            game.spaceship.captain_bridge.handle(message)
        elif game.state == CARGO_HOLD:
            game.spaceship.cargo_hold.handle(message)
        elif game.state == COMPUTER:
            game.spaceship.computer.handle(message)
        elif game.state == ESTRAD_PORT:
            game.estrad.port.handle(message)
        elif game.state == ESTRAD_SECURITY_SOLDIER:
            game.estrad.security_soldier.handle(message)
        elif game.state == ESTRAD_COLONY:
            game.estrad.colony.handle(message)
        elif game.state == ESTRAD_TRADER:
            game.estrad.trader.handle(message)
    elif message.text == '/start':
        games[message.chat.id] = Game(bot, games)
        games[message.chat.id].player_creation_menu.start(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_handle(call):
    game = games[call.message.chat.id]
    if game.state == INVENTORY:
        game.inventory.handle(call)


bot.polling()
