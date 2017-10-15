# Write a program to calculate the fixed monthly payment in order to pay off the balance.
balance = 999999
month = 12
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12

running_flag = True

low = balance / 12
high = balance * (1 + monthlyInterestRate)**12 / 12
monthlyPayment = (high + low) / 2

while running_flag:
    month = 12
    new_balance = balance
    while month > 0:
        unpaid_balance = round(new_balance - monthlyPayment, 2)
        interest = round(unpaid_balance * monthlyInterestRate, 2)
        new_balance = round(unpaid_balance + interest, 2)
        month -= 1
    if new_balance > 5:
        low = monthlyPayment
    elif new_balance < 0:
        high = monthlyPayment
    else:
        monthlyPayment = monthlyPayment + 0.1
        print('monthly payment is', round(monthlyPayment, 2))
        running_flag = False
    monthlyPayment = (low + high) / 2


