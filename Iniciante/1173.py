vetor = [0] * 10
i = int(input())

for j in range(10): 
    vetor[j] = i
    i *= 2
    print(f'N[{j}] = {vetor[j]}')