#Right down traingle
n = 5
i = n
while i >= 1:
    j = n
    while j > i:
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1
