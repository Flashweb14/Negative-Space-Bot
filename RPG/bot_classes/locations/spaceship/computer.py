from time import sleep
from datetime import datetime
from RPG.consts.game_states import COMPUTER
from RPG.bot_classes.base_handler import BaseHandler


class Computer(BaseHandler):
    def __init__(self, game, spaceship):
        super().__init__(game, COMPUTER)
        self.spaceship = spaceship

    def show(self, message):
        self.game.bot.send_message(message.chat.id, "Ты подходишь к бортовому компьютеру и запускаешь его")
        sleep(1)
        self.game.bot.send_message(message.chat.id, "_Spaceship Minisoft console: starting._",
                                   parse_mode='Markdown')
        sleep(1)
        self.game.bot.send_message(message.chat.id, "_Loading..._",
                                   parse_mode='Markdown')
        sleep(2)
        self.game.bot.send_message(message.chat.id,
                                   f"_Spaceship Minisoft console 3.8.2 _ {str(datetime.today())[:-7]}",
                                   parse_mode='Markdown')
        self.game.bot.send_message(message.chat.id, '_Введите "help", чтобы получить список основынх команд_',
                                   parse_mode='Markdown')

    def handle(self, message):
        if message.text == 'help':
            self.game.bot.send_message(message.chat.id,
                                       '*srp <ИМЯ ПЛАНЕТЫ>* _- установить маршрут на выбранную планету_ \n'
                                       '*sps inf eqp* _- посмотреть информацию о корабле и его снаряжении_ \n'
                                       '*cpi <ИМЯ ПЛАНЕТЫ>* _- посмотреть информацию о планете_ \n'
                                       '*pln* _- вывести список ближайших планет_ \n'
                                       '*plo* _- вывести спиок открытых планет_ \n'
                                       '*q* _- закрыть консоль Spaceship Minisoft_',
                                       parse_mode='Markdown')
        elif message.text.startswith('srp'):
            planet_name = message.text[4:].strip().capitalize()
            for planet in self.game.planets:
                if planet.name == planet_name:
                    self.game.current_planet = planet
                    self.game.bot.send_message(message.chat.id, f'Вы успешно прибыли на планету {planet_name}')
                    if planet not in self.game.opened_planets:
                        self.game.opened_planets.append(planet)
                else:
                    self.game.bot.send_message(message.chat.id, 'Невозможно проложить маршрут к данной планете. '
                                                                'Причина: планета не найдена')
        elif message.text.strip() == 'sps inf eqp':
            self.game.bot.send_message(message.chat.id, self.spaceship.get_info(), parse_mode='Markdown')
        elif message.text.startswith('cpi'):
            planet_name = message.text[4:].strip().capitalize()
            for planet in self.game.planets:
                if planet.name == planet_name:
                    self.game.bot.send_message(message.chat.id, planet.get_info(),
                                               parse_mode='Markdown')
                else:
                    self.game.bot.send_message(message.chat.id, 'Не удалось найти сведений о данной планете.')
        elif message.text.strip() == 'pln':  # TODO other planets
            if not self.game.current_planet:
                self.game.bot.send_message(message.chat.id, '🌎*Ближайшие планеты*\n'
                                                            '       - Эстрад',
                                           parse_mode='Markdown')
        elif message.text.strip() == 'plo':
            if self.game.opened_planets:
                opened_planets = '      -' + '\n      - '.join([str(planet) for planet in self.game.opened_planets])
                self.game.bot.send_message(message.chat.id, f'🌎Открытые планеты\n'
                                                            f'{opened_planets}')
            else:
                self.game.bot.send_message(message.chat.id, 'Вы пока не открыли ни одной планеты.',
                                           parse_mode='Markdown')
        elif message.text == 'q':
            self.game.bot.send_message(message.chat.id, '_Closing terminal..._',
                                       parse_mode='Markdown')
            sleep(1)
            self.game.bot.send_message(message.chat.id, '_Process finished with exit code -1_',
                                       parse_mode='Markdown')
            sleep(1)
            self.spaceship.captain_bridge.start(message)
        else:
            self.game.bot.send_message(message.chat.id, 'Введена неизвестная команда. Попробуйте ещё раз.')
