n1,n2,n3,n4=map(float,input().split())
def media(n1,n2,n3,n4):
    soma=(n1*2)+(n2*3)+(n3*4)+(n4*1)
    med= soma/10
    return med
def situacao():
    med = media(n1,n2,n3,n4)
    if med >= 7:
        return f'Media: {med:.1f}\nAluno aprovado.'
    elif med <= 4.9:
        return f'Media: {med:.1f}\nAluno reprovado.'
    else:
        n5=float(input())
        novamed= (med + n5)/2
        if novamed >= 5:
            return f'Media: {med:.1f}\nAluno em exame.\nNota do exame: {n5:.1f}\nAluno aprovado.\nMedia final: {novamed:.1f}'
        else:
            return f'Media: {med:.1f}\nAluno em exame.\nNota do exame: {n5:.1f}\nAluno reprovado.\nMedia final: {novamed:.1f}'    
print(situacao())                