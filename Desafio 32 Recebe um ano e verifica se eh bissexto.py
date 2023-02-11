from datetime import date
ano = int(input('\nInforme um ano para verificar se é Bissexto (coloque 0 para ano atual): '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print(f'O ano {ano} é BISSEXTO.\n')
else:
    print(f'O ano {ano} NÃO É BISSEXTO\n')