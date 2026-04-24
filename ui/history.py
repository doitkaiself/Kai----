import PySimpleGUI as sg
from templates.parts import u_font, normal_size

def create_history_window(data):
    headings = ['日付', '項目', '内容', '収入金額', '支払金額', '差引金額']

    layout = [
        [sg.Table(
            values=data,
            headings=headings,
            key = 'table',
            enable_events=True,
            auto_size_columns=True,
            justification='center',
            num_rows=10
        )],
        [sg.Button('編集', key='edit'), sg.Button('削除', key='delete'), sg.Button('戻る', key='back')]

    ]
    return sg.Window('履歴', layout, size=normal_size, finalize=True, font=u_font)
