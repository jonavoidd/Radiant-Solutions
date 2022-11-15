from food import Food
from getpass import getpass
from drinks import *

# initializing to ask wether user is admin and ask for it's password and ask if user is customer
admin = 1
password = 'password'
customer = 2
customer_payment = 0

# number of attempts admin can try to log in
attempts = 0 

# the business's tax
tax = 100/.12

print('[1] Admin \n[2] Customer \n[3] Exit')
user = int(input('Choose between 1 or 2: '))

while user != 3:
    # admin access
    if user == admin:
        while attempts < 3:
            pwd = str(getpass('\nPlease enter password: '))

            if pwd == password:
                print('\n\nWelcome back admin.')
            else:               
                print('\n\nWrong password! You only get  three chances to enter correct password.')
                attempts += 1  
                continue

            print('\n\n[1] Bills\n[2] Profits\n[3] Sales\n[4] Exit')

            admin_action = int(getpass(''))
        
            #using break for now as we wait for the data, i.e prices of foods, etc.
            if admin_action == 1:
                break
            elif admin_action == 2:
                break
            elif admin_action == 3:
                break
            else:
                break
        break

    # customer access
    # prompt customer to choose between order or exit
    elif user == customer:
        print('\n\nWelcome to our humble establishment our valued guest!')
        print('\n\n[1] Order \n[2] Exit')
        customer_action = int(getpass(''))

        while customer_action == 1:
            print("\n\nWhat2 do you want ma'am/sir? \n[1] Food \n[2] Beverage \n[3] Exit")
            customer_choice = int(getpass(''))

            if customer_choice == 1:
                print('[1] Main dish \n[2] Side dish \n[3] Desserts \n[4] Exit')
                customer_food = int(getpass(''))

                if customer_food == 1:
                    break
                elif customer_food == 2:
                    break
                elif customer_food == 3:
                    break
                elif customer_food == 4:
                    break
                else:
                    print('Invalid input')
                    break

            elif customer_choice == 2:
                print('[1] Caffeine \n[2] Juice \n[3] Softdrinks \n[4] Alcoholic \n[5] Exit')
                customer_drink = int(getpass(''))

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

    break


print(customer_payment)
print('\nThank you for using our program. Hope to see you again!')