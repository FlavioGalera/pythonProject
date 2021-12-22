from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um númeo entre 0 e 5, Tente Adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Você acertou! Parabens, me venceu')
else:
    print('Ganhei! pensei no número {} e não no número {}'.format(computador, jogador))
