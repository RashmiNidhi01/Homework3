#Nested loop
#for pattern (a)
print('(a)')
for i in range(0, 10):
    for j in range(0, i + 1):
        print("*", end=' ')
    print('')
print('')

    #pattern (b)
print('(b)')
for i in range(0, 10):
    for j in range(0, 10-i):
        print("*", end=' ')
    print('')
print('')

    #pattern (c)
print('(c)')
k = 2 * 10 - 2
k = -1
for i in range(10-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k = k + 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

    #Pattern (d)
k = 2 * 10 - 2
print("(d)")
for i in range(0, 10):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
            
