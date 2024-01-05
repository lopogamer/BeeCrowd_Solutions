salario = float(input())
def imposto(salario):
    if salario <= 2000:
        return 'Isento'
    elif salario <= 3000:
        return f'R$ {(salario - 2000) * 0.08:.2f}'
    elif salario <= 4500:
        return f'R$ {(salario - 3000) * 0.18 + 1000 * 0.08:.2f}'
    else:
        return f'R$ {(salario - 4500) * 0.28 + 1500 * 0.18 + 1000 * 0.08:.2f}'
print(imposto(salario))    