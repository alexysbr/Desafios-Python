total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('\nInforme o nome do produto: '))
    preco = float(input('Informe o preço do produto: R$ '))
    cont+=1
    total+=preco
    if preco > 1000:
        totmil+=1
    if cont == 1 or preco<menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi R$ {total:.2f}.')
print(f'Foram {totmil} produtos acima de R$ 1000.00.')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}\n')