x=int(input())
num = 1
for d in range(x):
    linha=[num,num*num,num*num*num,]
    linha2=[num,num*num+1,num*num*num+1]
    print(*linha)
    print(*linha2)
    num += 1