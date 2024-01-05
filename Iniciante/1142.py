x=int(input())
num = 1
for d in range(x):
    linha=[num,num+1,num+2,'PUM']
    print(*linha)
    num += 4