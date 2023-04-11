def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Valor inválido!\033[m')
        if ok:
            break
    return valor

#Programa principal
n = leiaInt('\nDigite um número inteiro: ')
print(f'O número digitado foi: {n}\n')