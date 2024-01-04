a , b = map(int, input().split())
def multiplos(a,b):
    if a % b == 0 or b % a == 0:
        return True
    else:
        return False
if multiplos(a,b):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
