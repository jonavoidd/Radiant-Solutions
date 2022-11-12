class Food:
    def __init__(self, price, portion, state):
        self.price = price 
        self.portion = portion
        self.state = state

    def get_price(self):
        return self.price

    def get_portion(self):
        return self.portion

    def get_state(self):
        return self.state