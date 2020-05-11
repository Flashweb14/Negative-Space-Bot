from os import environ
from telebot import TeleBot
from RPG.bot_classes.game import Game
# Импортирует все состояния игры
from RPG.consts.game_states import MAIN_MENU, INVENTORY, INVENTORY_INFO, CREATE_PLAYER_MENU, PLAYER_PROFILE, \
    CABIN, CAPTAIN_BRIDGE, CARGO_HOLD, COMPUTER, CREATE_SPACESHIP_MENU, ESTRAD_PORT, ESTRAD_SECURITY_SOLDIER, \
    ESTRAD_COLONY, ESTRAD_TRADER, EQUIPMENT, ESTRAD_TRADER_TRADE_MENU, ESTRAD_TRADER_BUY, ESTRAD_TRADER_SELL, \
    ESTRAD_FOREST_ENTRY, EQUIPMENT_WEAPON_INFO, EQUIPMENT_ARMOR_INFO, FIGHT_SYSTEM_PLAYER_TURN, \
    FIGHT_SYSTEM_WEAPON_USE, ESTRAD_FOREST_FIELD, FIGHT_SYSTEM_AIM_SHOT_MENU, ESTRAD_BAR, ESTRAD_FOREST_LAKE
from RPG.saves.data import db_session
from RPG.saves.data.games import DBGame

token = environ.get('TOKEN')  # Получает токен бота из конфигурации

bot = TeleBot(token)

db_session.global_init("saves/db/games.sqlite")
session = db_session.create_session()

games = {}
for game in session.query(DBGame).all():
    games[game.chat_id] = Game(bot, game.chat_id, game.player_name, game.spaceship_name, game.current_location,
                               game.state, game.player_inventory, game.player_money, game.player_hp, game.player_armor,
                               game.player_weapon, game.player_armor_set, game.player_laser_ammo,
                               game.fight_system_enemy, game.player_quest_items, game.fight_system_max_action_points,
                               game.fight_system_action_points, None)

for game_id in games:
    games[game_id].games = games


@bot.message_handler(content_types=['text'])  # Текстовый обработчик для состояний игры
def text_handle(message):
    if message.chat.id in games:
        game = games[message.chat.id]
        if game.state == CREATE_PLAYER_MENU:  # Регистрация пользователя, выбор имени и названия корабля
            game.player_creation_menu.handle(message)
        elif game.state == CREATE_SPACESHIP_MENU:
            game.spaceship_creation_menu.handle(message)

        elif game.state == MAIN_MENU:  # Главное меню
            game.main_menu.handle(message)

        elif game.state == INVENTORY:  # Инвентарь
            bot.send_message(message.chat.id, 'Не-а, здесь так нельзя.')
        elif game.state == INVENTORY_INFO:
            game.inventory_item_info.handle(message)

        elif game.state == PLAYER_PROFILE:  # Профиль игрока
            game.player_profile.handle(message)

        elif game.state == EQUIPMENT:  # Снаряжение игрока
            game.equipment.handle(message)
        elif game.state == EQUIPMENT_WEAPON_INFO:
            game.equipment_weapon_info.handle(message)
        elif game.state == EQUIPMENT_ARMOR_INFO:
            game.equipment_armor_info.handle(message)

        elif game.state == FIGHT_SYSTEM_PLAYER_TURN:  # Боевая система
            game.fight_system.player_turn.handle(message)
        elif game.state == FIGHT_SYSTEM_WEAPON_USE:
            game.fight_system.weapon_use_menu.handle(message)
        elif game.state == FIGHT_SYSTEM_AIM_SHOT_MENU:
            game.fight_system.aim_shot_menu.handle(message)

        elif game.state == CABIN:  # Локация "Космический корабль"
            game.spaceship.cabin.handle(message)
        elif game.state == CAPTAIN_BRIDGE:
            game.spaceship.captain_bridge.handle(message)
        elif game.state == CARGO_HOLD:
            game.spaceship.cargo_hold.handle(message)
        elif game.state == COMPUTER:
            game.spaceship.computer.handle(message)

        elif game.state == ESTRAD_PORT:  # Локация "Эстрад"
            game.estrad.port.handle(message)
        elif game.state == ESTRAD_SECURITY_SOLDIER:
            game.estrad.security_soldier.handle(message)

        elif game.state == ESTRAD_COLONY:  # Локация "Эстрад.Колония"
            game.estrad.colony.handle(message)
        elif game.state == ESTRAD_BAR:
            game.estrad.colony.bar.handle(message)
        elif game.state == ESTRAD_TRADER:
            game.estrad.colony.trader.handle(message)
        elif game.state == ESTRAD_TRADER_TRADE_MENU:
            game.estrad.colony.trader.trade_menu.handle(message)
        elif game.state == ESTRAD_TRADER_BUY:
            bot.send_message(message.chat.id, 'Не-а, здесь так нельзя.')
        elif game.state == ESTRAD_TRADER_SELL:
            bot.send_message(message.chat.id, 'Не-а, здесь так нельзя.')

        elif game.state == ESTRAD_FOREST_ENTRY:  # Локация "Эстрад.Лес"
            game.estrad.forest.entry.handle(message)
        elif game.state == ESTRAD_FOREST_FIELD:
            game.estrad.forest.field.handle(message)
        elif game.state == ESTRAD_FOREST_LAKE:
            game.estrad.forest.lake.handle(message)
        game.save(session)
    elif message.text == '/start':  # Обработчик команды /start, если игра ещё не начата
        games[message.chat.id] = Game(bot, message.chat.id, None, None, 'Колония', CREATE_PLAYER_MENU, '',
                                      500, 60, 0, '', '', 0, '', None, 1, 1, games)
        games[message.chat.id].player_creation_menu.start(message)
        game = games[message.chat.id]
        game.save(session)


@bot.callback_query_handler(func=lambda call: True)  # Call обработчик для состояний игры
def callback_handle(call):
    game = games[call.message.chat.id]
    if game.state == INVENTORY:  # Инвентарь
        game.inventory.handle(call)

    elif game.state == ESTRAD_TRADER_BUY:  # Торговец из локации "Эстрад.Колония"
        game.estrad.colony.trader.trade_menu.handle_buy(call)
    elif game.state == ESTRAD_TRADER_SELL:
        game.estrad.colony.trader.trade_menu.handle_sell(call)
    game.save(session)


bot.polling(none_stop=True)
