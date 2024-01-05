def impares(num,qtd):
    soma = 0
    while True:
        if qtd <= 0:
            break
        if num % 2 != 0:
            soma+= num
            qtd -= 1
        num += 1    
    return soma        
n = int(input())   
for _ in range(n):
    x,y = map(int,input().split())  
    soma = impares(x,y)
    print(soma)