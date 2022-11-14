from food import Food
from getpass import getpass

# initializing to ask wether user is admin and ask for it's password and ask if user is customer
admin = 1
password = 'password'
customer = 2

# number of attempts admin can try to log in
attempts = 0 

# the business's tax
tax = 100/.12

print('1 --- Admin ---\n2--- Customer ---\n')
user = int(getpass('Choose between 1 or 2:'))

while True:
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

            admin_action = int(getpass('\nWhich do you want to enter? '))
        
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

    if user == customer:
        print('\n\nWelcome to our humble establishment our valued guest!')
        print('1 --- Order \n2 --- Exit')
        print('Choose between 1 or 2')
        customer_action = int(input('Enter 1 or 2 '))

        if customer_action == 1:
            print("Which do you want ma'am/sir? \n1 --- Food \n2 --- Beverage")
            customer_choice = int(input('Choose between 1 and 2'))

        if customer_action == 2:
            break

        break
