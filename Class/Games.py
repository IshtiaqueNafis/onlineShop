from Class.Product import Product


class Games(Product):
    def __init__(self, id, name, price, description, system_game):
        super().__init__(id, name, price, description)
        if system_game is None:
            self.system_game = []  # this will contain 1 2 and 3 for system and games.
