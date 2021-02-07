from Class.Product import Product


class Accessories(Product):
    def __init__(self, id, name, price, description, acessory_for):
        super().__init__(id, name, price, description)
        self.acessory_for = acessory_for
