import PySimpleGUI as sg
from templates.parts import u_font, normal_size

accounting_items = ['交付金','振興費','会議費','雑収入','指導派遣費','通信事務所',' ','その他']


def create_input_window():


    
    layout = [
        [sg.Text('日付：', size=(12,1),justification='right'),
        sg.Input(key='text_date', size=(20,1)),
        sg.Push(),
        sg.CalendarButton('日付選択', format='%m-%d',key='button_calendar', target='text_date', size=(20,1))],

        [sg.Text('項目：', size=(12,1),justification='right'), sg.Listbox(values=accounting_items,key='list_item', 
                                    enable_events=True, size=(40,5))],

        [sg.Text('その他入力：', size=(12,1),justification='right'),sg.Input(key='other', disabled=True, size=(30,1))],

        [sg.Text('内容：', size=(12,1),justification='right'), sg.InputText(key='input_content', size=(30,1))],

        [sg.Text('収入金額：', size=(12,1),justification='right'), sg.InputText(key='input_income', enable_events=True, size=(20,1))],

        [sg.Text('支払金額：', size=(12,1),justification='right'), sg.InputText(key='input_expense', enable_events=True, size=(20,1))],

        [sg.Text('差引金額：', size=(12,1),justification='right'), sg.InputText(key='input_net',disabled=True, size=(20,1))],

        [sg.Push(),
        sg.Button('保存して次へ', size=(15,1)), 
        sg.Button('戻る',key='back', size=(15,1))]
        ]
    return sg.Window('帳簿入力',layout,size=normal_size, finalize=True, font=u_font, resizable=True)
    finalize=True 