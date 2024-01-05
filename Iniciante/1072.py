def impar(x,y):
    lista = []
    while True:
        if y <= 0:
            break
        if x % 2 != 0:
            y -= 1
            lista.append(x)
        x += 1    
    return lista    
x = int(input())
lista = impar(x,6)
for i in lista:
    print(i)
        