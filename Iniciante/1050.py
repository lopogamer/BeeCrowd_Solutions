ddd = {
    61: "Brasilia",
    71: "Salvador",
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte'
}
x=int(input())
if x in ddd:
    print(ddd[x])
else:
    print(f'DDD nao cadastrado')