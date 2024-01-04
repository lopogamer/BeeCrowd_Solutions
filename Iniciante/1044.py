a , b = map(int, input().split())
def multiplos(a,b):
    return bool(a % b == 0 or b % a == 0)
if multiplos(a,b):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
