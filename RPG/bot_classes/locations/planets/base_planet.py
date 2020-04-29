class BasePlanet:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_info(self):
        return f'*{self.name}*\n' \
               f'{self.description}'

    def start(self, message):
        self.port.start(message)

    def __str__(self):
        return self.name
