I = 0
J = 1
tmp = 0.2

while I <=1.8:
    for _ in range(3):
        if I in [0, 1] or I > 1.9:
            print(f"I={int(I)} J={int(J)}")
        else:
            print(f"I={I:.1f} J={J:.1f}")
        J += 1
    if I < 2.0:
        J = 1 + tmp
    else:
        J = 1
    I += 0.2
    tmp += 0.2
I = 2
for _ in range(3):
    print(f"I={int(I)} J={int(J)}")
    J += 1
