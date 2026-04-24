import PySimpleGUI as sg
from templates.parts import u_font, normal_size



def create_print_window():
    layout = [
        [sg.Text('ll', font=('Yu Gothic UI Semibold', 20))],
        [sg.Button('ll', size=(20,2))],
        [sg.Button('戻る', key='back', size=(20,2))]


    ]
    return sg.Window('印刷画面', layout, size=normal_size ,finalize=True, font=u_font)
