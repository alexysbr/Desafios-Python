from time import sleep
n1 = int(input('\nPrimeiro número: '))
n2 = int(input('Segundo número: '))
opcao = 0
while opcao != 5:
    print('''\n
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao = int(input('\nEscolha uma opção: '))
    if opcao ==1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opcao == 2:
        produto = n1*n2
        print(f'A multiplicação entre {n1} x {n2} é {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opcao == 4:
        n1 = int(input('\nPrimeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Encerrando...')
    else:
        print('Opção inválida!')
sleep(2)
print('Encerrado!\n')