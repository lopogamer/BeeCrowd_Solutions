x=float(input())
def inter(x):
    if x < 0 or x > 100:
        return 'Fora de intervalo'
    elif x >= 0 and x <= 25 :
        return 'Intervalo [0,25]'
    elif x >25 and x <= 50 :
        return 'Intervalo (25,50]'
    elif x > 50 and x <= 75:
        return 'Intervalo (50,75]'
    else:
        return 'Intervalo (75,100]'    
print(inter(x))  