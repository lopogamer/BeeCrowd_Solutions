nota1 = None
nota2 = None

while True:
    nota = float(input())

    if 0 <= nota <= 10:
        if nota1 is None:
            nota1 = nota
        else:
            nota2 = nota
            break
    else:
        print("nota invalida")

media = (nota1 + nota2) / 2
print(f"media = {media:.2f}")