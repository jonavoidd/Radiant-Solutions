# Module containing the class for drinks and the drinks

class Drinks:
    def __init__(self, price, state):
        self.price = price
        self.state = state

    def get_price(self):
        return self.price

    def get_state(self):
        return self.state


# cafe drinks
salted_caramel = Drinks(130.00, 'cold')
van_sweet_cream = Drinks(130.00, 'cold')
hot_choco = Drinks(155.00, 'hot')
white_hot_choco = Drinks(155.00, 'hot')
iced_choco = Drinks(155.00, 'cold')
steamed_milk = Drinks(120.00, 'hot')

# softdriks
coke = Drinks(32.00, 'cold')
sprite = Drinks(33.00, 'cold')
royal = Drinks(33.00, 'cold')

# juices
iced_tea = Drinks(30.00, 'cold')
four_seasons = Drinks(32.00, 'cold')
pineapple = Drinks(32.00, 'cold')
cucumber = Drinks(31.00, 'cold')

#alcohol
kahlua = Drinks(100.00, 'shot')
grey_goose = Drinks(350.00, 'shot')
jose_cuervo = Drinks(150.00, 'shot')
johnnie_walker = Drinks(400.00, 'shot')
chivas_regal = Drinks(300.00, 'shot')
jack_daniels = Drinks(320.00, 'shot')
hennessy = Drinks(500.00, 'shot')
the_botanist = Drinks(550.00, 'shpt')

