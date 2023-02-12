''' ate 9 anos mirim, ate 14 anos infantil, ate 19 anos junior, ate 25 anos senior, acima de 25 master '''

from datetime import date
atual = date.today().year
nascimento = int(input('\nInforme o ano de nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos.')
if idade<=9:
    print('Classificação Mirim!\n')
elif idade<=14:
    print('Classificação Infantil!\n')
elif idade<=19:
    print('Classificação Junior!\n')
elif idade<=25:
    print('Classificação Sênior!\n')
else:
    print('Classificação Master!\n')