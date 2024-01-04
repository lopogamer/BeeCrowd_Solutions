a , b, c = map(float, input().split())
def sao_triangulos(a,b,c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False
if sao_triangulos(a,b,c):
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")