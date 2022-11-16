# # Module containing the class for foods and the foods

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

    
#main_dish
butter_chicken= Food(300,'serve','hot')
spicy_pork_vindaloo= Food(300,'serve','hot')
sticky_tamarind_chicken= Food(300,'serve','hot')
palak_paneer= Food(300,'serve','hot')
crispy_pata= Food(300,'serve','hot')
    
    
#rice
basmati_rice= Food(50,'cup','hot')
scallion_rice= Food(50,'cup','hot')
white_rice= Food(50,'cup','hot')
mexican_rice= Food(50,'cup','hot')
pickled_rice= Food(50,'cup','hot')


#side_dish
green_salad= Food(120,'serve','hot')
roasted_veggies= Food(120,'serve','hot')
mashed_potatoes= Food(120,'serve','hot')
green_beans= Food(120,'serve','hot')
pickled_beets= Food(120,'serve','hot')
     
    
#pastas
lasagne= Food(150,'serve','hot')
carbonara= Food(150,'serve','hot')
vegetable_pasta= Food(150,'serve','hot')
ravioli= Food(150,'serve','hot')
macaroni_cheese= Food(150,'serve','hot')

    
#pastries
cranberry_muffins= Food(100,'serve','hot')
capuccino_muffins= Food(100,'serve','hot')
monkey_bread= Food(100,'serve','hot')
beignets= Food(100,'serve','hot')
caramel_rolls= Food(100,'serve','hot')
    
 
#soups   
gazpacho= Food(120,'serve','hot')
harira= Food(120,'serve','hot')
minestrom= Food(120,'serve','hot')
laksa= Food(120,'serve','hot')
caldo_verde= Food(120,'serve','hot')
                   
                   
#desserts
brownie_sundae= Food(120,'serve','cold')
coffee_pie= Food(120,'serve','cold')
leche_flan= Food(120,'serve','cold')
grasshopper_pie= Food(120,'serve','cold')
hazzlenut_pops= Food(120,'serve','cold')
