vetor = [0] * 20

i = 19

while i >= 0:
    vetor[i] = int(input())
    i -= 1
for i in range(20):
    print(f'N[{i}] = {vetor[i]}')