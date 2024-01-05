v=str(input())
t=str(input())
h=str(input())
def animal(v,t,h):
    if v == 'vertebrado':
        if t == 'ave':
            if h == 'carnivoro':
                return 1
            else:
                return 2
        if t == 'mamifero':
            if  h == 'onivoro':
                return 3
            else:
                return 4
    elif v == 'invertebrado':
        if t == 'inseto':
            if h == 'hematofago':
                return 5
            else:
                return 6
        if t == 'anelideo':
            if h == 'hematofago':
                return 7
            else:
                return 8
    else:
        return 0
animais={
    1: 'aguia',
    2: 'pomba',
    3: 'homem',
    4: 'vaca',
    5: 'pulga',
    6: 'lagarta',
    7: 'sanguessuga',
    8: 'minhoca'
}    
x = animal(v,t,h)
print(animais[x])