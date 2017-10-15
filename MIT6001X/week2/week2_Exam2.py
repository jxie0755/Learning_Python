# Write a program to calculate the fixed monthly payment in order to pay off the balance.
balance = 999999
month = 12
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12

monthlyPayment = 0
running_flag = True

while running_flag:
    new_balance = balance
    month = 12
    while month > 0:
        unpaid_balance = round(new_balance - monthlyPayment, 2)
        interest = round(unpaid_balance * monthlyInterestRate, 2)
        new_balance = round(unpaid_balance + interest, 2)
        month -= 1
    if new_balance >= 0:
        monthlyPayment += 10
    else:
        print('Lowest Payment:', monthlyPayment)
        running_flag = False

