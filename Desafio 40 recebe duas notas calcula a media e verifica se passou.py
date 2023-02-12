# Se a media for abaixo de 5 reprovado, se entre 5 e 6,9 recuperacao e se cima de 6,9 foi aprovado.

nota1 = float(input('\nInforme a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1+nota2)/2
print(f'A média do aluno foi: {media}')
if 7>media>=5:
    print('O aluno está de Recuperação!\n')
elif media<5:
    print('O aluno foi Reprovado!\n')
elif media>=7:
    print('O aluno foi Aprovado!\n')