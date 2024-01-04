segundos = int(input())
def horas(segundos):
    return segundos // 3600
def minutos(segundos):
    return (segundos % 3600) // 60
def segundo(segundos):
    return (segundos % 3600) % 60
print(f"{horas(segundos)}:{minutos(segundos)}:{segundo(segundos)}")
