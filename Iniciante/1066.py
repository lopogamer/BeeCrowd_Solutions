contpares = 0
contimpar =0
contneg = 0
contpos = 0
def ioup(x):
    if x % 2 == 0:
        return 'par'
    else:
        return 'impar'
def posouneg(x):
    if x > 0:
        return 'p'
    elif x < 0:
        return 'n'
        
for _ in range(1,6):
    x = int(input())
    a = ioup(x)
    
    if a == 'par':
        contpares += 1
    elif a != 'par':
        contimpar += 1 
    b = posouneg(x)
    if b == 'p':
        contpos += 1
    elif b == 'n':
        contneg += 1
print(f'{contpares} valor(es) par(es)\n{contimpar} valor(es) impar(es)\n{contpos} valor(es) positivo(s)\n{contneg} valor(es) negativo(s)')
