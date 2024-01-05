tentativas=int(input())
coelhos=0
ratos=0
sapos=0
for _ in range(tentativas):
    qntd,animal=input().split(" ", 1)
    qntd=int(qntd)
    if animal == "C":
        coelhos += qntd
    elif animal == "R":
        ratos += qntd
    else:
        sapos += qntd
total= (coelhos+sapos+ratos)
print(f'Total: {total} cobaias')         
print(f"Total de coelhos: {coelhos}\nTotal de ratos: {ratos}\nTotal de sapos: {sapos}")
animais=[coelhos,ratos,sapos]
animais1=["coelhos","ratos","sapos"]
for x ,animal in zip(animais,animais1):
    x1= x / total
    percentual= x1 * 100
    print(f'Percentual de {animal}: {percentual:.2f} %')