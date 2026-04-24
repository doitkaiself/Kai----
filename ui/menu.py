import PySimpleGUI as sg
from templates.parts import u_font



def create_menu_window():
    layout = [
        [sg.Text('メニュー', font=('Yu Gothic UI Semibold', 20))],
        [sg.Button('新規作成',key='create', size=(20,2))],
        [sg.Button('履歴を見る', key='history', size=(20,2))],
        [sg.Button('印刷する', key='print', size=(20,2))],
        [sg.Button('アプリを閉じる', key='close', size=(20,2))]

    ]
    return sg.Window('メニュー', layout, size=(800,600) ,finalize=True, font=u_font)
