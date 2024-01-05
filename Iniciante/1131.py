gremio=0
inter=0
empates=0
grenais=0
while True:
    i,g=map(int,input().split())
    if i > g:
        inter += 1
        grenais += 1
    elif g > i:
        gremio += 1
        grenais += 1
    else:
        empates += 1
        grenais += 1       
    print('Novo grenal (1-sim 2-nao)')
    resposta=int(input())
    if resposta != 1:
        break
print(f'{grenais} grenais')
print (f'Inter:{inter}')
print(f"Gremio:{gremio}")
print (f"Empates:{empates}")
if inter > gremio:
    print("Inter venceu mais") 
else:
    print('Gremio venceu mais')