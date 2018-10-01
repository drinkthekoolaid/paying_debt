"""
A quick program finding the monthly rate in order to pay down debt in one year
"""

balance = 999999
annualInterestRate = 0.18

monthlyinterest = annualInterestRate / 12
tempbalance = balance
epsilon = 0.01
monthlypay = tempbalance / 12
lowp = tempbalance / 12
highp = (tempbalance * (1 + monthlyinterest)**12) / 12.0

while abs(balance) > epsilon:
    balance = tempbalance
    monthlypay = (lowp + highp) / 2
    for i in range(12):   
        unpaidbalance = balance - monthlypay
        interest = unpaidbalance * (annualInterestRate / 12)
        balance = unpaidbalance + interest   
    if balance > epsilon:
        lowp = monthlypay

    elif balance < epsilon:
        highp = monthlypay

    else:
        break
        
print(round(monthlypay, 2))
