from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import FIGHT_SYSTEM_AIM_SHOT_MENU


class AimShotMenu(BaseHandler):
    def __init__(self, game):
        super().__init__(game, FIGHT_SYSTEM_AIM_SHOT_MENU)
        self.reply_keyboard.row('😡 Голова - 5 ОД')
        self.reply_keyboard.row('🧥 Тело - 3 ОД')
        self.reply_keyboard.row('🦵🏻 Конечности - 4 ОД')
        self.reply_keyboard.row('⬅️ Назад')

    def show(self, message):
        self.game.bot.send_message(message.chat.id, 'Выбери в какую часть тела будешь целиться.')
        self.game.bot.send_message(message.chat.id,
                                   f'Доступно очков действия: *{self.game.fight_system.action_points}*',
                                   parse_mode='Markdown', reply_markup=self.reply_keyboard)

    def handle(self, message):
        if message.text == '😡 Голова - 5 ОД':
            if self.game.fight_system.action_points >= 5:
                if self.game.player.laser_ammo >= 1:
                    self.game.player.attack(self.game.fight_system.enemy, 3, 9)
                else:
                    self.game.fight_system.show_ammo_error(message)
            else:
                self.game.fight_system.show_action_points_error(message, self.reply_keyboard)
        elif message.text == '🧥 Тело - 3 ОД':
            if self.game.fight_system.action_points >= 3:
                if self.game.player.laser_ammo >= 1:
                    self.game.fight_system.player_attack(message, 1, 3, 7, 3, self.reply_keyboard)
                else:
                    self.game.fight_system.show_ammo_error(message)
            else:
                self.game.fight_system.show_action_points_error(message, self.reply_keyboard)
        elif message.text == '🦵🏻 Конечности - 4 ОД':
            if self.game.fight_system.action_points >= 4:
                if self.game.player.laser_ammo >= 1:
                    self.game.fight_system.player_attack(message, 1, 3, 5, 5, self.reply_keyboard)
                else:
                    self.game.fight_system.show_ammo_error(message)
            else:
                self.game.fight_system.show_action_points_error(message, self.reply_keyboard)
        elif message.text == '⬅️ Назад':
            self.game.fight_system.weapon_use_menu.start(message)
        else:
            self.show_input_error(message)
