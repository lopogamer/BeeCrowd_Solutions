inicial, final = map(int, input().split())
def tempo(inicial, final):
    if inicial == final:
        return 'O JOGO DUROU 24 HORA(S)'
    elif inicial > final:
        return f'O JOGO DUROU {24 - inicial + final} HORA(S)'
    else:
        return f'O JOGO DUROU {final - inicial} HORA(S)'
print(tempo(inicial, final))