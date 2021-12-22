salario = float(input('Digite o Salário: '))
aumento = salario * 15 / 100
total = salario + aumento
print(f'O seu salario é de R${salario:.2f}\nSeu Aumento foi de R${aumento:.2f}\nSeu novo salário ja com 15% de rajuste é de R${total:.2f}')
