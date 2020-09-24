Paid=2
change=(100-Paid)
q=25
d=10
n=5
p=1
q=int(change//q)
change-= d*q
d=int(change//d)
change-= d*d
n=int(change//n)
change-= d*n
p=int(change//p)
change-= d*p
print('Your change is:')
print(f'{q} quarters\n{d} dimes\n{n} nickles\n{p} pennies')

p=0
n=0
d=0
q=0
paid=1
money=(100-paid)
if money>=25:
    p=money/25
    money=money%25
if  money>=10:
    n=money/10
    money=money%10

if money>=5:
    d=money/5
    money=money%5

if money>=0:
    q=money/1
    money=0

print('Your change is:')
print(f'{q} quarters\n{d} dimes\n{n} nickles\n{p} pennies')