x=int(input())
num = 1
for d in range(x):
    linha=[num,num*num,num*num*num,]
    print(*linha)
    num += 1