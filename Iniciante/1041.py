x,y=map(float,input().split())
def quadrante(x,y):
    if x == 0 and y !=0:
        return 'Eixo Y'
    elif y == 0 and x !=0:
        return 'Eixo X'
    elif (x+y)==0:
        return 'Origem'
    elif x > 0 and y > 0:
        return 'Q1'   
    elif x < 0 and y > 0:
        return'Q2' 
    elif x < 0 and y < 0:
        return 'Q3'
    else:
        return "Q4"
print(quadrante(x,y))          
