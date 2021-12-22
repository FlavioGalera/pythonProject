funcionario = str(input('Qual o seu nome: '))
salario = float(input('Valor do seu salário: '))
aumento = salario * (15 / 100)
if salario <= 1250.00:
    print("Seu salario teve um auemto de 15%, seu salario novo é de R$ {}".format(aumento))
if salario > 1250.00:
    aumento = salario * (10 / 100)
    print("Seu salario teve um aumento de 10%, seu salario novo é de R$ {}".format(aumento))


