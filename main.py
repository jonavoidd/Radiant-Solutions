from food import *
from getpass import getpass
from drinks import *
from tax import tax_calcu
from bills import *

# initializing to ask wether user is admin and ask for it's password and ask if user is customer
admin = 1
password = 'password'
customer = 2
customer_payment = 0

# number of attempts admin can try to log in
attempts = 0 

print('[1] Admin \n[2] Customer \n[3] Exit')
user = int(input('Choose between 1 or 2: '))

while user != 3:
    # admin access
    if user == admin:
        while attempts < 3:
            try:
                pwd = str(getpass('\nPlease enter password: '))
                if pwd == password:
                    print('\n\nWelcome back admin.')
                else:               
                    print('\n\nWrong password! You only get  three chances to enter correct password.')
                    attempts += 1  
                    continue
            except:
                print('Please check your input')

            print('\n\n[1] Bills\n[2] Profits\n[3] Sales\n[4] Tax \n[5] Exit')

            admin_action = int(getpass(''))
        
            # Actions an admin can do
            if admin_action == 1:
                print(f'BILLS \n\nElectric: ₱{electricity.get_bills()} \
                    \nWater: ₱{water.get_bills()}')
                break

            elif admin_action == 2:
                sales = float(input('Please enter your sales: '))
                costs = float(input('Enter costs: '))
                print(f'Your profit is ₱{profit(sales, costs)}')
                break

            elif admin_action == 3:
                sales = float(input('Please enter your sales: '))
                print(f'Your sales is ₱{sale(sales)}')
                break

            elif admin_action == 4:
                income = float(input("Please enter your monthly income: "))
                tax_calcu(income)
                continue

            elif admin_action == 5:
                break
            else:
                print('Invalid input')
            break
        break

    # customer access
    # prompt customer to choose between order or exit
    elif user == customer:
        print('\n\nWelcome to our humble establishment our valued guest!')
        print('\n\n[1] Order \n[2] Exit')
        customer_action = int(getpass(''))

        while customer_action == 1:
            print("\n\nWhat do you want ma'am/sir? \n[1] Food \n[2] Beverage \n[3] Exit")
            customer_choice = int(getpass(''))

            if customer_choice == 1:
                print('[1] Main dish \n[2] Side dish \n[3] Desserts \n[4] Pasta \n[5] Exit')
                customer_food = int(getpass(''))

                # Options for main dish
                if customer_food == 1:
                    print(f'[1] Butter Chicken = {butter_chicken.get_price()} \
                        \n[2] Spicy Pork Vindaloo = {spicy_pork_vindaloo.get_price()} \
                        \n[3] Sticky Tamarind Chicken = {sticky_tamarind_chicken.get_price()} \
                        \n[4] Palak Paneer = {palak_paneer.get_price()} \
                        \n[5] Crispy Pata = {crispy_pata.get_price()}')

                    user_chose_mainDish = int(getpass(''))   
                    if user_chose_mainDish == 1:
                        customer_payment += butter_chicken.get_price()
                    elif user_chose_mainDish == 2:
                        customer_payment += spicy_pork_vindaloo.get_price()
                    elif user_chose_mainDish == 3:
                        customer_payment += sticky_tamarind_chicken.get_price()
                    elif user_chose_mainDish == 4:
                        customer_payment += palak_paneer.get_price()
                    elif user_chose_mainDish == 5:
                        customer_payment += crispy_pata.get_price()
                    else:
                        print("Invalid Input")

                # Options for side dish
                elif customer_food == 2:
                    print(f'[1] Green Salad = {green_salad.get_price()} \
                        \n[2] Roasted Veggies = {roasted_veggies.get_price()} \
                        \n[3] Mashed Potatoes = {mashed_potatoes.get_price()} \
                        \n[4] Green Beans = {green_beans.get_price()} \
                        \n[5] Pickled Beets = {pickled_beets.get_price()}')
                    
                    user_chose_sideDish = int(getpass(''))
                    if user_chose_sideDish == 1:
                        customer_payment += green_salad.get_price()
                    elif user_chose_sideDish == 2:
                        customer_payment += roasted_veggies.get_price()
                    elif user_chose_sideDish == 3:
                        customer_payment += mashed_potatoes.get_price()
                    elif user_chose_sideDish == 4:
                        customer_payment += green_beans.get_state()
                    elif user_chose_sideDish == 5:
                        customer_payment += pickled_beets.get_price()
                    else:
                        print("Invalid Input")

                # Options for desserts
                elif customer_food == 3:
                    print(f'[1] Brownie Sundae =  {brownie_sundae.get_price()} \
                        \n[2] Coffee Pie = {coffee_pie.get_price()} \
                        \n[3] Leche Flan = {leche_flan.get_price()} \
                        \n[4] Grasshopper Pie = {grasshopper_pie.get_price()} \
                        \n[5] Hazzlenut Pops = {hazzlenut_pops.get_price()}')

                    user_chose_desserts = int(getpass(''))
                    if user_chose_desserts == 1:
                        customer_payment += brownie_sundae.get_price()
                    elif user_chose_desserts == 2:
                        customer_payment += coffee_pie.get_price()
                    elif user_chose_desserts == 3:
                        customer_payment += leche_flan.get_price()
                    elif user_chose_desserts == 4:
                        customer_payment += grasshopper_pie.get_price()
                    elif user_chose_desserts == 5:
                        customer_payment += hazzlenut_pops.get_price()
                    else:
                        print("Invalid Input")

                # Options for pastas
                elif customer_food == 4:
                    print(f'[1] Lasagne = {lasagne.get_price()} \
                        \n[2] Carbonara = {carbonara.get_price()} \
                        \n[3] Vegetable Pasta = {vegetable_pasta.get_price()} \
                        \n[4] Ravioli = {ravioli.get_portion()} \
                        \n[5] Macaroni Cheese = {macaroni_cheese.get_price()}')

                    user_chose_pastas = int(getpass(''))
                    if user_chose_pastas == 1:
                        customer_payment += lasagne.get_price()
                    elif user_chose_pastas == 2:
                        customer_payment += carbonara.get_price()
                    elif user_chose_pastas == 3:
                        customer_payment += vegetable_pasta.get_price()
                    elif user_chose_pastas == 4:
                        customer_payment += ravioli.get_price()
                    elif user_chose_pastas == 5:
                        customer_payment += macaroni_cheese.get_price()
                    else:
                        print("Invalid Input")
                elif customer_food ==5:
                    break
                else:
                    print('Invalid input')
                    break

            elif customer_choice == 2:
                print('[1] Caffeine \n[2] Juice \n[3] Softdrinks \n[4] Alcoholic \n[5] Exit')
                customer_drink = int(getpass(''))

                # Options for caffeine
                if customer_drink == 1:
                    print(f'[1] Salted Caramel = {salted_caramel.get_price()} \
                        \n[2] Vanilla Sweet Cream = {van_sweet_cream.get_price()} \
                        \n[3] Hot Choco = {hot_choco.get_price()} \
                        \n[4] White Hot Choco = {white_hot_choco.get_price()} \
                        \n[5] Iced Choco = {iced_choco.get_price()} \
                        \n[6] Steamed Milk = {steamed_milk.get_price()}')
                    
                    user_chose_cafe = int(getpass(''))
                    if user_chose_cafe == 1:
                        customer_payment += salted_caramel.get_price()
                    elif user_chose_cafe == 2:
                        customer_payment += van_sweet_cream.get_price()
                    elif user_chose_cafe == 3:
                        customer_payment += hot_choco.get_price()
                    elif user_chose_cafe == 4:
                        customer_payment += white_hot_choco.get_price()
                    elif user_chose_cafe == 5:
                        customer_payment += iced_choco.get_price()
                    elif user_chose_cafe == 6:
                        customer_payment += steamed_milk.get_price()
                    else:
                        print('Invalid input')

                # Options for Juice
                elif customer_drink == 2:
                    print(f'[1] Iced Tea = {iced_tea.get_price()} \
                        \n[2] Four Seasons = {four_seasons.get_price()} \
                        \n[3] Pineapple = {pineapple.get_price()} \
                        \n[4] Cucumber = {cucumber.get_price()}')

                    user_chose_juice = int(getpass(''))
                    if user_chose_juice == 1:
                        customer_payment += iced_tea.get_price()
                    elif user_chose_juice == 2:
                        customer_payment += four_seasons.get_price()
                    elif user_chose_juice == 3:
                        customer_payment += pineapple.get_price()
                    elif user_chose_juice == 4:
                        customer_payment += cucumber.get_price()
                    else:
                        print('Invalid input')
                
                # Options for softdrinks
                elif customer_drink == 3:
                    print(f'[1] Coke = {coke.get_price()} \
                        \n[2] Sprite = {sprite.get_price()} \
                        \n[3] Royal = {royal.get_price()}')

                    user_chose_soft = int(getpass(''))
                    if user_chose_soft == 1:
                        customer_payment += coke.get_price()
                    elif user_chose_soft == 2:
                        customer_payment += sprite.get_price()
                    elif user_chose_soft == 3:
                        customer_payment += royal.get_price()
                    else:
                        print('Invalid input')

                # Options for alcoholic beverages
                elif customer_drink == 4:
                    print(f'[1] Kahlua = {kahlua.get_price()} \
                        \n[2] Grey Goose Vodka = {grey_goose.get_price()} \
                        \n[3] Jose Cuervo = {jose_cuervo.get_price()} \
                        \n[4] Johnnie Walker = {johnnie_walker.get_price()} \
                        \n[5] Chivas Regal = {chivas_regal.get_price()} \
                        \n[6] Jack Daniels = {jack_daniels.get_price()} \
                        \n[7] Hennessy = {hennessy.get_price()} \
                        \n[8] The Botanist = {the_botanist.get_price()}')

                    user_chose_alco = int(getpass(''))
                    if user_chose_alco == 1:
                        customer_payment += kahlua.get_price()
                    elif user_chose_alco == 2:
                        customer_payment += grey_goose.get_price()
                    elif user_chose_alco == 3:
                        customer_payment += jose_cuervo.get_price()
                    elif user_chose_alco == 4:
                        customer_payment += johnnie_walker.get_price()
                    elif user_chose_alco == 5:
                        customer_payment += chivas_regal.get_price()
                    elif user_chose_alco == 6:
                        customer_payment += jack_daniels.get_price()
                    elif user_chose_alco == 7:
                        customer_payment += hennessy.get_price()
                    elif user_chose_alco == 8:
                        customer_payment += the_botanist.get_price()
                    else:
                        print('Invalid input')

                # To exit
                elif customer_drink == 5:
                    break                
                else:
                    print('Invalid Input')
                    break
                
            elif customer_choice == 3:
                break
            else:
                print('Invalid input')

        else:
            break

    print(f'Your total bill is ₱{round(customer_payment, 2)}')
    tries = 0

    while tries < 3:
        payment = float(input('Please enter your money: ₱'))
        change = payment - customer_payment
        if change >= 0:
            print(f'Your change is ₱{round(change, 2)}')
            break
        else:
            print(f'Not enough money! you need ₱{customer_payment - payment} more')
            tries += 1
            continue
        
    print('\n\nThank you for using our program. Hope to see you again!')
    break