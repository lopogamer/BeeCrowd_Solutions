a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
valores=[a,b,c,d,e]
for x in range(len(valores)):
    valores[x] = abs(valores[x])
contador= 0
for x in valores:
    if x &2 ==0:
        contador+=1
        if x == 0:
            contador += 1
print(f'{contador} valores pares')
    