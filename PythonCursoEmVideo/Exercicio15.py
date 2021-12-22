km = float(input('Quantos km percorridos?: '))
distancia = km * 0.15
print(f'O valor a ser pago em km é de R${distancia:.2f}')

dia = int(input('Quantos dias ele foi alugado?: '))
diaria = 60 * dia
print(f'O valor a ser pago por este(s) dia(s) é de R${diaria:.2f}')

print(f'você tem que pagar R${distancia+diaria:.2f}')
