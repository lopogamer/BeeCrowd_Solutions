a,b,c,d=map(int,input().split())
def valor(a,b,c,d):
    if  b > c and d > a:
        if c + d > a + b:
            if c > 0 and d > 0:
                if a % 2 ==0:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0
    
x = valor(a,b,c,d)
if x == 1:
    print(f'Valores aceitos')
else:
    print(f'Valores nao aceitos') 