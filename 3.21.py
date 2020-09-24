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