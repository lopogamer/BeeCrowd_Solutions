n = int(input())
for i in range(n):
    pa,pb,txa,txb = input().split()
    pa , pb = map(int,(pa,pb))
    txa,txb = map(float,(txa,txb))
    anos = 0
    while True:
        if anos > 100:
            break
        novapa = int(((txa / 100) * pa) + pa )
        novapb = int(((txb / 100) * pb) + pb )
        anos += 1
        if novapa > novapb:
            break
        pa = novapa
        pb = novapb
    if anos > 100:
        print(f'Mais de 1 seculo.')
    else:
        print(f'{anos} anos.')