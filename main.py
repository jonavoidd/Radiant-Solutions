from food import Food
from getpass import getpass

admin = 1
password = 'password'
customer = 2

print("1 ---admin---\n2 ---customer---\n")
user = int(getpass("Choose between 1 or 2:"))

while True:
    if user == admin:
        pwd = str(getpass("\nPlease enter password: "))
        
        if pwd == password:
            print("\n\nWelcome back admin.")
            print("\n1 ---Bills\n2 ---Profits\n3 ---Sales")

            admin_action = int(getpass("Which do you want to enter? "))
        
            #using break for now as we wait for the data, i.e prices of foods, etc.
            if admin_action == 1:
                break
            if admin_action == 2:
                break
            if admin_action == 3:
                break
        
        else:
            print("\n\nWrong password!")
            break

    if user == customer:
        print("\n\nWelcome to our humble establishment our valued guest!")
        break
