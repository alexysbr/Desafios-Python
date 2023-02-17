from random import randint
v = 0
while True:
    jogador = int(input('Informe um número: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, dando um total de {total}.')
    print ('Deu Par!!\n' if total%2 == 0 else 'Deu Ímpar!!\n')
    if tipo =='P':
        if total%2 == 0:
            print('Você venceu!!')
            v+=1
        else:
            print('Você perdeu! Mais sorte da próxima vez!')
            break
    if tipo == 'I':
        if total%2==1:
            print('Você venceu!!')
            v+=1
        else:
            print('Você perdeu! Mais sorte da próxima vez!')
            break
print(f'\nGame Over! Você venceu {v} vez(es).\n')
            