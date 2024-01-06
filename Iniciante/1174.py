vetorA = [0] * 100
for i in range(100):
    vetorA[i] = float(input())
    if vetorA[i] <= 10:
        print(f'A[{i}] = {vetorA[i]:.1f}')