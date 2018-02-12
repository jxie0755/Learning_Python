# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12

month = 12
while month > 0:
    minimum_payment = round(balance * monthlyPaymentRate, 2)
    unpaid_balance = round(balance - minimum_payment, 2)
    interest = round(unpaid_balance * monthlyInterestRate, 2)
    balance = round(unpaid_balance + interest, 2)
    print('remaining balance is', balance)
    month -= 1

print('Remaining balance:', balance)

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

   
