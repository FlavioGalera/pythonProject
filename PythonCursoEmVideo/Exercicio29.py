velociadade = float(input('Qual a velocidade do carro?: '))
if velociadade > 80:
    print('MULTADO!: Você excedeu o limite permitido, que é de 80km/h')
    multa = (velociadade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com cuidado!')
