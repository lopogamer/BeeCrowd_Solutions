cont= 0
lista=[]
for x in range(1,7):
    num =input()
    num = float(num)
    if num > 0:
        cont += 1
        lista.append(num)
print(f'{cont} valores positivos')
soma=0
for x in lista:
    soma += x
qntd=len(lista)
media= soma / qntd
print (f"{media:.1f}")