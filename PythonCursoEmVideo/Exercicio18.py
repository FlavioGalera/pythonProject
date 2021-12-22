import math
angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O angulo é {angulo}\nO angulo de {angulo } tem o seno de {seno:.2f}\nO angulo de {angulo} tem o cosseno de {cosseno:.2f}\n'
      f'O angulo de {angulo} tem a tangente de {tangente:.2f}')
