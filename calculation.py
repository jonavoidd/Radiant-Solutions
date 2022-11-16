def payment():
    money = float(input())

def ask_toPay():
    ready = input("Ready to pay? Type 'No' to end: ")
    if ready == 'No' or ready == 'no':
        return False
    else:
        return True

    ctr = 0
    while ctr <= 1:    
        while ask_toPay() is True:
            money_given = payment()
            money_needed = customer_payment
            money_left = money_given - money_needed
            new_money = round(money_left, 2)
            print(f'₱{new_money} is your change.')
        ctr += 1