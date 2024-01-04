dias = int(input())

def anos(dias):
    return dias // 365
def meses(dias):
    return (dias % 365) // 30
def dia(dias):
    return (dias % 365) % 30
print(f"{anos(dias)} ano(s)")
print(f"{meses(dias)} mes(es)")
print(f"{dia(dias)} dia(s)")
