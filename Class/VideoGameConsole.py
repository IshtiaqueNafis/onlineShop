from Class.Product import Product


class VideoGameConsole(Product):
    def __init__(self, id, name, price, description, company_name, release_date):
        super().__init__(id, name, price, description)
        self.release_date = release_date
        self.company_name = company_name
