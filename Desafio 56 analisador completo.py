'''Recebe nome, idade, sexo, de 4 pessoas, devolve a media de idade, o nome do homem mais velho e a quantidade de mulheres menores de 20 anos'''

somaidade = 0
mediaidade= 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print(f'----{p}ª PESSOA ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade>maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade/4
print ( f'A média de idade é {mediaidade} anos.')
print (f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print (f'Ao todo são {totmulher20} mulhere(s) abaixo de 20 anos.\n')