hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

def duracao(hora_inicial, minuto_inicial, hora_final, minuto_final):
    if hora_inicial == hora_final and minuto_inicial == minuto_final:
        return 'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)'
    elif hora_inicial == hora_final and minuto_inicial > minuto_final:
        return f'O JOGO DUROU 23 HORA(S) E {60 - minuto_inicial + minuto_final} MINUTO(S)'
    elif hora_inicial == hora_final and minuto_inicial < minuto_final:
        return f'O JOGO DUROU 0 HORA(S) E {minuto_final - minuto_inicial} MINUTO(S)'
    elif hora_inicial > hora_final and minuto_inicial == minuto_final:
        return f'O JOGO DUROU {24 - hora_inicial + hora_final} HORA(S) E 0 MINUTO(S)'
    elif hora_inicial > hora_final and minuto_inicial > minuto_final:
        return f'O JOGO DUROU {24 - hora_inicial + hora_final - 1} HORA(S) E {60 - minuto_inicial + minuto_final} MINUTO(S)'
    elif hora_inicial > hora_final and minuto_inicial < minuto_final:
        return f'O JOGO DUROU {24 - hora_inicial + hora_final} HORA(S) E {minuto_final - minuto_inicial} MINUTO(S)'
    elif hora_inicial < hora_final and minuto_inicial == minuto_final:
        return f'O JOGO DUROU {hora_final - hora_inicial} HORA(S) E 0 MINUTO(S)'
    elif hora_inicial < hora_final and minuto_inicial > minuto_final:
        return f'O JOGO DUROU {hora_final - hora_inicial - 1} HORA(S) E {60 - minuto_inicial + minuto_final} MINUTO(S)'
    elif hora_inicial < hora_final and minuto_inicial < minuto_final:
        return f'O JOGO DUROU {hora_final - hora_inicial} HORA(S) E {minuto_final - minuto_inicial} MINUTO(S)'
print(duracao(hora_inicial, minuto_inicial, hora_final, minuto_final))