nome = input('Digite seu Nome: ')
idade = int( input('Digite sua Idade: '))
altura = float( input("DIgite sua Altura: "))
peso = float( input('Digite seu Peso: '))
ano_atual = int(input('Digite Ano Atual: '))
data_nascimento = (ano_atual) - (idade)
imc = peso / (altura ** 2)
print(f'{nome} tem {idade} anos, {altura} de altura.')
print(f'{nome} pesa {peso}kg, o Imc de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {data_nascimento}')
