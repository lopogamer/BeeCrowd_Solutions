def fibbonaci(x):
    if x == 0:
        print('0')
    elif x == 1:
        print('0 1')
    else:
        print('0 1', end=' ')
        a = 0
        b = 1
        for i in range(2, x):
            c = a + b
            a = b
            b = c
            if i == x - 1:
                print(c)
            else:
                print(c, end=' ')
x = int(input())
fibbonaci(x)