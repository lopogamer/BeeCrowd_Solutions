vetor = [0] * 1000
i = 0
x = int(input())
k = x
while i < 1000:
    vetor[i] = x - k
    k -= 1
    if k == 0:
        k = x
    i += 1
for i in range(1000):
    print(f'N[{i}] = {vetor[i]}')
      