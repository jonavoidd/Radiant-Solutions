class Drinks:
    def __init__(self, price, state):
        self.price = price
        self.state = state

    def get_price(self):
        return self.price

    def get_state(self):
        return self.state


# cafe drinks
salted_caramel = Drinks(130, 'cold')
van_sweet_cream = Drinks(130, 'cold')
hot_choco = Drinks(155.00, 'hot')
white_hot_choco = Drinks(155.00, 'hot')
iced_choco = Drinks(155.00, 'cold')
steamed_milk = Drinks(120.00, 'hot')

# softdriks
coke = Drinks(32, 'cold')
sprite = Drinks(33, 'cold')
royal = Drinks(33, 'cold')

# juices
iced_tea = Drinks(30, 'cold')
four_seasons = Drinks(32, 'cold')
pineapple = Drinks(32, 'cold')
cucumber = Drinks(31.50, 'cold')

#alcohol
kahlua = Drinks(100, 'shot')
grey_goose = Drinks(350, 'shot')
jose_cuervo = Drinks(150, 'shot')
johnnie_walker = Drinks(400, 'shot')
chivas_regal = Drinks(300, 'shot')
jack_daniels = Drinks(320, 'shot')
hennessy = Drinks(500, 'shot')
the_botanist = Drinks(550, 'shpt')
