tentativas=int(input())
soma=0
for _ in range(tentativas):
    x,y=map(int,input().split())
    temp_soma=0
    if y > x:
        for d in range(x+1,y):
            if d %2 != 0:
                temp_soma += d
    elif x > y:
        for d in range(y+1,x):
            if d %2 != 0:
                temp_soma += d
    print(temp_soma)