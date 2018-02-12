# A summary of the required math is found below:

# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

# We provide sample test cases below. We suggest you develop your code on your own machine, and make sure your code passes the sample test cases, before you paste it into the box below.


monthlyInterestRate = annualInterestRate / 12

month = 12
while month > 0:
    minimum_payment = round(balance * monthlyPaymentRate, 2)
    unpaid_balance = round(balance - minimum_payment, 2)
    interest = round(unpaid_balance * monthlyInterestRate, 2)
    balance = round(unpaid_balance + interest, 2)
    month -= 1

print('Remaining balance:', balance)


# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

# In this problem, we will not be dealing with a minimum monthly payment rate.

# The following variables contain values as described below:

# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

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
        
        
# You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)

# Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!

# The following variables contain values as described below:

# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What is a reasonable lower bound for this payment value? $0 is the obvious anwer, but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.

# What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for an entire year.

# In short:

# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

# Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.

# Note that if you do not use bisection search, your code will not run - your code only has 30 seconds to run on our servers.


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
