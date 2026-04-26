import PySimpleGUI as sg


def custom_calendar():
    layout = [
        [sg.CalendarButton('日付選択', target='-DATE-', format='%Y-%m-%d', size=(20,2), font=('Yu Gothic UI', 16)),
        sg.Input(key='-DATE-', size=(20,1))]
    ]
    win = sg.Window('カレンダー', layout, modal=True)

    event, values = win.read()
    win.close()

    return values['-DATE-']