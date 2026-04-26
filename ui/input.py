import PySimpleGUI as sg
from templates.parts import u_font, normal_size
from datetime import datetime

today = datetime.now()
accounting_items = ['交付金','振興費','会議費','雑収入','指導派遣費','通信事務所','その他']

def create_input_window():
    layout = [
        [sg.Text('日付：', size=(10,1), justification='right'),
        sg.Spin([i for i in range(1,13)],initial_value=today.month,key='month',size=(5,1),font=u_font),
        sg.Text('月'),
        sg.Spin([i for i in range(1, 32)],initial_value=today.day,key='day',size=(5,1),font=u_font),
        sg.Text('日')
        ],

        [sg.Text('項目：', size=(12,1), justification='right'),
        sg.Listbox(values=accounting_items, key='list_item',
                    enable_events=True, size=(40,5), font=u_font)],

        [sg.Text('その他入力：', size=(12,1), justification='right'),
        sg.Input(key='other', disabled=True, size=(30,1), font=u_font)],

        [sg.Text('内容：', size=(12,1), justification='right'),
        sg.InputText(key='input_content', size=(30,1), font=u_font)],

        [sg.Text('収入金額：', size=(12,1), justification='right'),
        sg.InputText(key='input_income', enable_events=True, size=(20,1), font=u_font)],

        [sg.Text('支払金額：', size=(12,1), justification='right'),
        sg.InputText(key='input_expense', enable_events=True, size=(20,1), font=u_font)],

        [sg.Text('差引金額：', size=(12,1), justification='right'),
        sg.InputText(key='input_net', disabled=True, size=(20,1), font=u_font)],

        [sg.Push(),
        sg.Button('保存して次へ', size=(15,1), font=u_font),
        sg.Button('戻る', key='back', size=(15,1))]
    ]

    

    return sg.Window('帳簿入力', layout, size=normal_size, finalize=True, font=u_font, resizable=True)