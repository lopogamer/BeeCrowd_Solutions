while True:
    cont = 0
    lista = []
    x = int(input())
    if x == 0:
        break
    while True:
        if cont == 5:
            break
        if x % 2 == 0:
            lista.append(x)
            cont += 1
        x += 1
        
    resultado = sum(lista)
    print(resultado)