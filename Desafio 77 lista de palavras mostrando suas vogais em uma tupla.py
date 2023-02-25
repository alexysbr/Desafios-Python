palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'grátis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais:   ', end='')
    for letra in p:        
        if letra.lower() in 'aáeiou':
            print(letra.upper(), end='  ')
print('\n')