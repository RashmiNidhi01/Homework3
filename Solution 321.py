quarters=0
dimes=0
nickles=0
pennies=0
dollars=100
price=82
change = dollars - price
balance = change

if balance>=25:
  quarters = int(change/25)
  pennies = change % 25
  balance = change - (25 * quarters)

if balance>=10:
  dimes = int(balance/10)
  pennies = pennies % 10
  balance = balance - (10 * dimes)

if balance>=5:
  nickles = int(balance/5)
  pennies = pennies % 5
  balance = balance - (5 * nickles)

if balance>=0:
  pennies = int(balance/1)
  

print('Your total change is:', change)
print('quarters', quarters)
print('dimes', dimes)
print('nickles', nickles)
print('pennies', pennies)
