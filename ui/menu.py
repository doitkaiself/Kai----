import PySimpleGUI as sg
from templates.parts import menu_font,normal_size

def create_menu_window():
    menu_column = sg.Column(
        [
            [sg.Text('メニュー', font=menu_font)],
            [sg.Button('新規作成', key='create', size=(20,2), font=menu_font)],
            [sg.Button('履歴を見る', key='history', size=(20,2), font=menu_font)],
            [sg.Button('印刷する', key='print', size=(20,2), font=menu_font)],
            [sg.Button('アプリを閉じる', key='close', size=(20,2), font=menu_font)]
        ],
        element_justification='center'
    )

    layout = [
        [sg.VPush()],
        [sg.Push(), menu_column, sg.Push()],
        [sg.VPush()]
    ]

    return sg.Window(
        'メニュー',
        layout,
        size=normal_size,
        finalize=True,
        font=menu_font,
        resizable=True
    )