import random
n1 = str(input('primeiro nome: '))
n2 = str(input('segundo nome: '))
n3 = str(input('terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'O escolhido é {escolhido}')

