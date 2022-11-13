from food import Food
from getpass import getpass

admin = 1
password = 'password'
customer = 2
attempts = 0 # number of attempts admin can try to log in

print("1 --- Admin ---\n2 --- Customer ---\n")
user = int(getpass("Choose between 1 or 2:"))

while True:
    if user == admin:
        while attempts < 3:
            pwd = str(getpass("\nPlease enter password: "))
            if pwd == password:
                print("\n\nWelcome back admin.")
        
            else:               
                print("\n\nWrong password!")
                attempts += 1  
                continue

            print("\n1 --- Bills\n2 --- Profits\n3 --- Sales\n4 --- Exit")

            admin_action = int(getpass("Which do you want to enter? "))
        
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
        print("\n\nWelcome to our humble establishment our valued guest!")
        break
