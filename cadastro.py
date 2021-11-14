from PySimpleGUI import PySimpleGUI as sg
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuário', size=(20, 1))],
    [sg.Text('Senha'),sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login')],
    [sg.Button('Entrar')]
]
janela = sg.Window('Tela de login', layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.Window_Closed:
        break
    if eventos == 'Entrar':
        if valores['usuário'] == 'flavio' and valores['senha'] == '123456':
            print('Bem vindo!')


