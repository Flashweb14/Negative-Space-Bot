import telebot
from RPG.bot_classes.game import Game
from RPG.game_states import MAIN_MENU, INVENTORY, INVENTORY_INFO, ZERO_STATE, NONE_STATE, REGISTRATION, PLAYER_PROFILE, \
    CABIN, CAPTAIN_BRIDGE, CARGO_HOLD, COMPUTER, CREATE_SPACESHIP, ESTRAD_PORT, ESTRAD_SECURITY_SOLDIER

bot = telebot.TeleBot('TOKEN')
game = Game(bot)


@bot.message_handler(content_types=['text'])
def text_handle(message):
    if message.chat.id in game.players:
        player = game.players[message.chat.id]
        if player.state == ZERO_STATE:
            pass
        elif player.state == REGISTRATION:
            game.player_creation_menu.handle(message)
        elif player.state == CREATE_SPACESHIP:
            game.spaceship_creation_menu.handle(message)
        elif player.state == MAIN_MENU:
            game.main_menu.handle(message)
        elif player.state == INVENTORY:
            bot.send_message(message.chat.id, 'Не-а, это здесь не работает')
        elif player.state == INVENTORY_INFO:
            game.inventory_item_info.handle(message)
        elif player.state == PLAYER_PROFILE:
            game.player_profile.handle(message)
        elif player.state == CABIN:
            game.spaceship[message.chat.id].cabin.handle(message)
        elif player.state == CAPTAIN_BRIDGE:
            game.spaceship[message.chat.id].captain_bridge.handle(message)
        elif player.state == CARGO_HOLD:
            game.spaceship[message.chat.id].cargo_hold.handle(message)
        elif player.state == COMPUTER:
            game.spaceship[message.chat.id].computer.handle(message)
        elif player.state == ESTRAD_PORT:
            game.estrad[message.chat.id].port.handle(message)
        elif player.state == ESTRAD_SECURITY_SOLDIER:
            game.estrad[message.chat.id].security_soldier.handle(message)
        elif message.text == '/main_menu':
            game.main_menu.show(message)
            game.players[message.chat.id].state = MAIN_MENU
    elif message.text == '/start':
        game.start_new_game(message)
        game.player_creation_menu.start(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_handle(call):
    player = game.players[call.message.chat.id]
    if player.state == INVENTORY:
        game.inventory.handle(call)


bot.polling()
