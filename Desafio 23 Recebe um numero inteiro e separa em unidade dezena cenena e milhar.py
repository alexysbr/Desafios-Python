num = int(input('Digite um número de 0 a 9999: '))
u = num // 1%10
d = num // 10%10
c = num // 100%10
m = num // 1000%10
print(f'Analisando o número {num}')
print(f'A unidade deste número é: {u}')
print(f'A dezena deste número é: {d}')
print(f'A centena deste número é: {c}')
print(f'O milhar deste número é: {m}')