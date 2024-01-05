n = int(input())
for i in range (n+1):
    if i % 2 == 0 and i > 0:
        f = i ** 2
        print(f'{i}^2 = {f}')