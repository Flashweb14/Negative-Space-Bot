from RPG.consts.game_states import ESTRAD_TRADER, ESTRAD_TRADER_TRADE_MENU, ESTRAD_TRADER_BUY, ESTRAD_TRADER_SELL
from RPG.bot_classes.base_dialog import BaseDialog
from RPG.consts.quest_items import FEDERATION_PASS
from RPG.consts.weapons import LIGHT_LASER_RIFFLE, OLD_LASER_PISTOL
from RPG.consts.items import LITTLE_MED_PACK
from RPG.bot_classes.trader import TradeMenu


class EstradTrader(BaseDialog):
    def __init__(self, game):
        super().__init__(game, ESTRAD_TRADER, 'Солдат Межгалактической Республики', 'Здравия желаю! Здесь '
                                                                                    'ты можешь получить базовый '
                                                                                    'комплект солдата федерации, если у'
                                                                                    ' тебя есть удостоверение, или '
                                                                                    'купить дополнительное снаряжение,'
                                                                                    ' если базового тебе недостаточно.',
                         '👨🏼')
        self.reply_keyboard.row('Покажи мне свои товары')
        self.reply_keyboard.row('Хочу получить комплект')
        self.reply_keyboard.row('Мне пора')
        self.kit_given = False
        self.trade_menu = TradeMenu(game, self, ESTRAD_TRADER_TRADE_MENU, ESTRAD_TRADER_BUY, ESTRAD_TRADER_SELL,
                                    'Вот, посмотри, '
                                    'что у меня есть.',
                                    [LITTLE_MED_PACK, OLD_LASER_PISTOL], 1.25)

    def handle(self, message):
        if message.text == 'Покажи мне свои товары':
            self.trade_menu.start(message)
        elif message.text == 'Хочу получить комплект':
            if FEDERATION_PASS in self.game.player.quest_items:
                if not self.kit_given:
                    self.game.player.add_item(LIGHT_LASER_RIFFLE)
                    self.game.player.add_item(LITTLE_MED_PACK)
                    self.kit_given = True
                    self.say(message, 'Вот, пожалуйста. Добро пожаловать в ряды колонизаторов планеты Эстрад!')
                else:
                    self.say(message, "По одному комплекту на руки, ты свой уже получил.")
            else:
                self.say(message, 'Прости, без пропуска солдата федерации я не могу выдать тебе боевой комплект.')
        elif message.text == 'Мне пора':
            self.say(message, 'Заходи ещё.')
            self.game.estrad.colony.start(message)
        else:
            self.show_input_error(message)
