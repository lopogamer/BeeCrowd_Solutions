alcool=0
gasolina=0
dielsel=0
etc=0
while True:
    x=int(input())
    if x == 4:
        break
    elif x == 1:
        alcool += 1
    elif x == 2:
        gasolina += 1
    elif x == 3:
        dielsel += 1
    else:
        etc += 1
print(f'MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gasolina}\nDiesel: {dielsel}')