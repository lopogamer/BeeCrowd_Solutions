n1=None
n2=None
while True:
    x = input()
    x = float(x)
    if x < 0 or x > 10: 
        print('nota invalida')
    if 0 <= x <= 10:
        if n1 == None:
            n1 = x
        elif n2 == None:
            n2 = x 
            med = (n1+n2)/2
            print(f'media = {med:.2f}')
            while True:
                print('novo calculo (1-sim 2-nao)')
                y= int(input())
                if y == 1:
                    n1=None
                    n2=None
                    break 
                elif y == 2:
                    break
            if y == 2:
                break