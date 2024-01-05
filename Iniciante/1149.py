Lista  = list(map(int, input().split()))
A = Lista[0]
for I  in Lista[1:]:
    if I > 0:
        N = I
        break
Soma = 0
for I in range(N):
    Soma += A + I
print(Soma)