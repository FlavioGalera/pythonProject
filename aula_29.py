"""
primeiro_nome = input("Digite seu primeiro nome: ")
primeiro_nome = len(primeiro_nome)
if primeiro_nome <= 4:
    print('Seu nome é curto')
elif primeiro_nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
"""



horario = input('digite a horario (0 - 23): ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Horario deve estar entre (0-23): ')
    else:
        if horario <= 11:
            print("Bom Dia")
        elif horario <= 17:
            print('Boa Tarde')
        else:
            print('Boa Noite')
else:
    print('Por favor, digite um horario entre 0 e 23.')

"""
numero_inteiro = input('Digite um numero inteiro: ')

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é par')
    else:
        print(f'{numero_inteiro} é impar')
else:
        print('Isso não é um numero inteiro.')
"""
