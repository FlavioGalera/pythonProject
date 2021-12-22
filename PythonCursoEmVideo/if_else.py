n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
m = (n1+n2+n3)/3
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi Boa! Parabéns!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')