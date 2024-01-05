x=int(input())
y=int(input())
if x > y:
    x,y=y,x
for d in range(x+1,y):
    if d > 0:
        if d %5 == 2 or d %5 == 3:
            print(d)