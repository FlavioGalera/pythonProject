distancia = float(input('Qual a distância da sua viagem: '))
print('Você esta preste a começar uma viagem de {:.2f}km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('O preço da sua passagem será de R$ {:.2f}'.format(preço))
