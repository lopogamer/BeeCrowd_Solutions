s = 1 
k = 3
l = 2
while True:
    s = s + (k/l)
    k += 2
    l *= 2
    if k == 39:
        break
print(f'{s:.2f}')