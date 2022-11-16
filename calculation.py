def payment():
    money = float(input("Please enter your payment: "))
    print(f'you paid {money}')

def total():
    cost = float(input("Your total payment is: "))

def ask_toPay():
    ready = input("Ready to pay? Type 'No' to end: ")
    if ready == 'No':
        return False
    else:
        return True
        
while ask_toPay():
    money_given = payment()
    money_needed = total()
    money_left = money_given - money_needed
    new_money = round(money_left, 2)
    print(f"You have ₱{new_money} left. ")