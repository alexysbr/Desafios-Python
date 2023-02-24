cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('\nDigite um número de 0 a 20: '))
    if 0<=num<=20:
        break
    print('[Erro] Número inválido. Tente novamente.')    
print(f'O seu número por extenso é: {cont[num].upper()}\n')