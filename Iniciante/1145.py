x, y = map(int, input().split())
tmp = x

for i in range(1, y + 1):
    if tmp > 1:
        print(i, end=' ')
        tmp -= 1
    else:
        print(i , end = '\n')
        tmp = x
