import PySimpleGUI as sg
from templates.parts import u_font, normal_size, button_size

def create_history_window(data):
    
    headings = ['日付', '項目', '内容', '収入金額', '支払金額', '差引金額']

    layout = [
        
        [sg.Table(
            values=data,
            headings=headings,
            key = 'table',
            enable_events=True,
            auto_size_columns=False,
            justification='center',
            num_rows=20,
            col_widths=[12, 10, 20, 12, 12, 12],
            
        )],
        [
        sg.Button('編集', key='edit', size=button_size, font=u_font), 
        sg.Button('削除', key='delete', size=button_size, font=u_font),
        sg.Button('戻る', key='back', size=button_size, font=u_font)
        ]

    ]
    return sg.Window('履歴', layout, size=normal_size, finalize=True, font=u_font)
