codigo, quantidade=map(int,input().split())
tabela={
    1: 4.0,
    2: 4.5,
    3: 5.0,
    4: 2.0,
    5: 1.5
    }
preco=tabela[codigo]    
valor= preco * quantidade
print(f'Total: R$ {valor:.2f}')