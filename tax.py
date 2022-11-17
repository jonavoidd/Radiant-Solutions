def tax_calcu(income):
    if income <= 10000:   
        tax = income * .05

    elif income <= 30000: 
        tax = income * .10

    elif income <= 70000: 
        tax = income * .15
    else:
        tax = income * .30

    print(f'you owe {round(tax, 2)} pesos in tax!')
