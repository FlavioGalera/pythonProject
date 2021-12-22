produto = float(input("Digite o preço: "))
desconto = produto*5/100
total_desconto = produto - desconto
print(f'O valor do produto é de R$ {produto:.2f}\nO valor do desconto é de R$ {desconto:.2f}\nO valor com desconto é de R$ {total_desconto:.2f}')
