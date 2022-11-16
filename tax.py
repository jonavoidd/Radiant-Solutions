while True:
    try:

        income = int(input("Please enter your monthly income: "))
    except ValueError:
        print("Sorry,  please enter taxable income as a number")

        continue
    else:
        break


if income <= 0-10000:   
    tax = 5

elif income <= 30000: 
    tax = (income - 10000) * .10

elif income <= 70000: 
    tax = (income - 10000) * .15
else:
    tax = (income - 10000) * .30

print("you owe", tax, "pesos in tax!")