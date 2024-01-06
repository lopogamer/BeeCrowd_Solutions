n = int(input())
def fibonacci(n):
    vetor = [0] * n
    for i in range(n):
        if i == 0:
            vetor[i] = 0
        elif i == 1:
            vetor[i] = 1
        else:
            vetor[i] = vetor[i - 1] + vetor[i - 2]
    return vetor
vetor = fibonacci(61)
for _ in range(n):
    i = int(input())
    print(f'Fib({i}) = {vetor[i]}')
    