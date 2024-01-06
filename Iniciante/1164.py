n = int(input())
for _ in range(n):
    lista = []
    x = int(input())
    for i in range(1,x):
        if x % i == 0:
            lista.append(i)
    if sum(lista) == x:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')