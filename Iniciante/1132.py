soma=0
x=int(input())
y=int(input())
if x > y:
    x,y=y,x
for d in range(x,y+1):
    if d %13 != 0:
        soma += d
print(soma)