from random import randint
from time import sleep
computador = randint(1,5) #Faz o computador pensar em um número
print('-=-'*21)
print('Vou pensar em um número entre 1 e 5. Tente adivinhar...')
print('-=-'*20, computador)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else :
    print('Não foi dessa vez, mais sorte da próxima vez!')