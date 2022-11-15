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

            print('\n\n1 --- Bills\n2 --- Profits\n3 --- Sales\n4 --- Exit')

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
        print('\n\n1 --- Order \n2 --- Exit')
        customer_action = int(getpass(''))

        if customer_action == 1:
            print("\n\nWhat2 do you want ma'am/sir? \n1 --- Food \n2 --- Beverage")
            customer_choice = int(getpass(''))

            if customer_choice == 1 :
                print('1 --- main dish \n2 --- side dish \n3 --- desserts \n4 --- exit')
                customer_food = int(getpass(''))

                if customer_food == 1:
                    break
                elif customer_food == 2:
                    break
                elif customer_food == 3:
                    break
                else:
                    break
            elif customer_choice == 2:
                print('1 --- caffeine \n2 --- juice \n3 --- softdrinks \n4 --- alcoholic')
                customer_drink = int(getpass(''))

                if customer_drink == 1:
                    print(f'Salted Caramel = {salted_caramel.get_price()} \
                        \nVanilla Sweet Cream = {van_sweet_cream.get_price()} \
                        \nHot Choco = {hot_choco.get_price()} \
                        \nWhite Hot Choco = {white_hot_choco.get_price()} \
                        \nIced Choco = {iced_choco.get_price()} \
                        \nsteamed milk = {steamed_milk.get_price()}')
                        
                elif customer_drink == 2:
                    break
                elif customer_drink == 3:
                    break
                else:
                    break
            else:
                print('Invalid input')

        else:
            break

    break

print('\nThank you for using our program. Hope to see you again!')