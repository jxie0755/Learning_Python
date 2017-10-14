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

