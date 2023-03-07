def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

# Programa Principal
escreva('Prof. Gustavo Guanabara')
escreva('Curso em Vídeo de Python!')
while True:
    texto = input('Digite uma mensagem (0 para sair): ')   
    if texto in '0':
        break
    escreva(texto)
print()
