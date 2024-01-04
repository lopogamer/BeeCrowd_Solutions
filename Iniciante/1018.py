valor = int(input())

def nota_100(valor):
    return valor // 100
def nota_50(valor):
    return (valor % 100) // 50
def nota_20(valor):
    return ((valor % 100) % 50) // 20
def nota_10(valor):
    return (((valor % 100) % 50) % 20) // 10
def nota_5(valor):
    return ((((valor % 100) % 50) % 20) % 10) // 5
def nota_2(valor):
    return (((((valor % 100) % 50) % 20) % 10) % 5) // 2
def nota_1(valor):
    return ((((((valor % 100) % 50) % 20) % 10) % 5) % 2) // 1
print(valor)
print(f"{nota_100(valor)} nota(s) de R$ 100,00")
print(f"{nota_50(valor)} nota(s) de R$ 50,00")
print(f"{nota_20(valor)} nota(s) de R$ 20,00")
print(f"{nota_10(valor)} nota(s) de R$ 10,00")
print(f"{nota_5(valor)} nota(s) de R$ 5,00")
print(f"{nota_2(valor)} nota(s) de R$ 2,00")
print(f"{nota_1(valor)} nota(s) de R$ 1,00")