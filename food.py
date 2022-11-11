class FoodPrice:
    def __init__(self, price, portion):
        self.price = price 
        self.portion = portion

    def get_price(self):
        return self.price

    def get_amount(self):
        return self.portion

