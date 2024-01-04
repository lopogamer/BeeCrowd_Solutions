a,b,c=map(int,input().split())
valores=[a,b,c]
lista= sorted(valores,reverse=False)
for x in lista:
    print(x)
print()    
for x in valores:
    print(x)