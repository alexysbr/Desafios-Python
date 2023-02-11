a = int(input('\nPrimeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#Verifcando quem é menor
menor = a
if b<=a and b<=c:
    menor = b
if c<=a and c<=b:
    menor = c

#verificando quem é maior
maior = a
if b>=a and b>=c:
    maior = b
if c>=a and c>=b:
    maior = c

print(f'\nO menor valor é {menor}.')
print(f'O maior valor é {maior}\n')