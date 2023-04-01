def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :parâmetro n: número para calcular seu fatorial.
    :parâmetro show: (opcional) para mostrar ou não a conta.
    :return: retorna o valor do fatorial.
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            if c>1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#programa principal
print()
print(fatorial(5, show=True))
print()
help(fatorial)