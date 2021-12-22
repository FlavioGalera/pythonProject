altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede:  '))
area = altura * largura
tinta = area / 2
print(f'A parede tem {altura} mt de altura x {largura} mt de largura.\nSua area é de {area:.2f} mt para ser pintado.\nVai ser usado {tinta:.2f}L de tinta para pintar essa parede. ')
