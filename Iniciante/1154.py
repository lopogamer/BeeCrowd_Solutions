lista = []
while True:
    x = int(input())
    if x < 0:
        break
    lista.append(x)
media = sum(lista)/len(lista)
print(f'{media:.2f}')