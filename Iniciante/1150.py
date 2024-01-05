x = int(input())
while True:
    y = int(input())
    if y > x:
        break
Soma = 0
cont = 0
i = x
while True:
    Soma += i
    cont += 1
    if Soma > y:
        break
    i += 1
print(cont)