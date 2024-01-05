temp_soma=0
temp_lista=[]
while True:
    x,y=map(int,input().split())
    if x <= 0 or y <= 0:
        break
    temp_soma=0
    temp_lista=[]    
    if x > y:
        x, y = y, x
    for d in range(x,y+1):
        temp_soma += d
        temp_lista.append(d)
    for k in temp_lista:
            print(k,end = " ")  
    print(f"Sum={temp_soma}")