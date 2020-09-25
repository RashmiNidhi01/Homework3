#for pattern (a)
print('')
for i in range(0, 5):
    for j in range(0, i + 1):
        print("*", end=' ')
    print('')
print('')

#For pattern (b)
print('')
for i in range(0, 5):
    for j in range(0, 5-i):
        print("*", end=' ')
    print('')
print('')

#For pattern (c)
print(' ')
k = -1
for i in range(5-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k = k + 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("")

#For Pattern (d)
print("")
for i in range(0, 5):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
            
