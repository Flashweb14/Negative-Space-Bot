import telebot
from RPG.bot_classes.bot_game import BotGame
from RPG.game_states import MAIN_MENU, INVENTORY, INVENTORY_INFO, ZERO_STATE, NONE_STATE, REGISTRATION, PLAYER_PROFILE, \
    MAIN_STREET, MAIN_STREET_TRADER, MAIN_STREET_TRADER_BUY, MAIN_STREET_TRADER_SELL, RUINED_HOUSE, RUINED_HOUSE_BOX, \
    CABIN, CAPTAIN_BRIDGE, CARGO_HOLD

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
            bot_game.inventory_item_info.handle(message)
        elif game.state == PLAYER_PROFILE:
            bot_game.player_profile.handle(message)
        elif game.state == MAIN_STREET:
            bot_game.main_street_location[message.chat.id].handle(message)
        elif game.state == MAIN_STREET_TRADER:
            bot_game.main_street_location[message.chat.id].trader.handle(message)
        elif game.state == MAIN_STREET_TRADER_BUY:
            bot.send_message(message.chat.id, 'Не-а, это здесь не работает')
        elif game.state == MAIN_STREET_TRADER_SELL:
            bot.send_message(message.chat.id, 'Не-а, это здесь не работает')
        elif game.state == RUINED_HOUSE:
            bot_game.ruined_house_location[message.chat.id].handle(message)
        elif game.state == RUINED_HOUSE_BOX:
            bot_game.ruined_house_location[message.chat.id].box.handle(message)
        elif game.state == CABIN:
            bot_game.spaceship[message.chat.id].cabin.handle(message)
        elif game.state == CAPTAIN_BRIDGE:
            bot_game.spaceship[message.chat.id].captain_bridge.handle(message)
        elif game.state == CARGO_HOLD:
            bot_game.spaceship[message.chat.id].cargo_hold.handle(message)
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
    elif game.state == MAIN_STREET_TRADER_BUY:
        bot_game.main_street_location[call.message.chat.id].trader.handle_buy(call)


bot.polling()
