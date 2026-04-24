import PySimpleGUI as sg

from ui.menu import create_menu_window
from ui.input import create_input_window
from ui.history import create_history_window 
from ui.input import accounting_items
from db.database import history_data, edit_index
from logic.check import is_number
from ui.print import create_print_window

current_window = create_menu_window()
sg.theme('TealMono')







while True:
    event, values = current_window.read()
    
    if event in (sg.WIN_CLOSED, 'アプリを閉じる'):
        break
    #--------
    #画面遷移
    #--------

    elif event == 'create':
        current_window.close()
        current_window = create_input_window() #最初に作った入力画面へ

    elif event == 'history':
        current_window.close()
        current_window = create_history_window(history_data) #履歴画面へ    

    elif event == 'print':
        current_window.close()
        current_window = create_print_window() #印刷画面へ
    
    elif event == 'back':
        current_window.close()
        current_window = create_menu_window() #戻る
    

    #--------
    #履歴編集
    #--------

    elif event == '編集':
        selected = values['table']
        if not selected:
            sg.popup('選択してください' \
            '')
            continue
        
        edit_index = selected[0]
        record = history_data[edit_index]

        current_window.close()
        current_window = create_input_window()

        #入力画面に履歴の値をセット
        current_window['text_date'].update(value=record[0])
        current_window['input_content'].update(value=record[2])
        current_window['input_income'].update(value=(record[3]))
        current_window['input_expense'].update(value=(record[4]))
        current_window['input_net'].update(value=(record[5]))

        if record[1] in accounting_items:
            current_window['list_item'].update(set_to_index=[accounting_items.index(record[1])])
        else:
            current_window['list_item'].update(set_to_index=[accounting_items.index('その他')])
            current_window['other'].update(value=record[1], disabled=False)

    #--------
    #入力画面の処理
    #--------

    #その他が選ばれたら入力欄を有効化
    if event == 'list_item':
        if values['list_item'] and values['list_item'][0] == 'その他':
            current_window['other'].update(disabled=False)
        else:
            current_window['other'].update(disabled=True)
            current_window['other'].update(value='') #リセット

    #差引金額を計算して表示       
    if event in ('input_income', 'input_expense'):
            income = values['input_income']
            expense = values['input_expense']
            if income.isdigit() and expense.isdigit():
                net = int(income) - int(expense)
                current_window['input_net'].update(value=str(net))
            else:
                current_window['input_net'].update('')

    #保存して次へ
    if event == '保存して次へ':
        
        #キーの内容
        entry_content = values['input_content']
        entry_calander = values['text_date']
        income = values['input_income']
        expense = values['input_expense']

        #入力内容のバリデーション
        if not entry_calander:
            sg.popup('日付を選択してください')
            continue

        if not values['list_item']:
            sg.popup('項目を選択してください')
            continue

        if not values['input_content']:
            sg.popup('内容を入力してください')
            continue

        if values['list_item']:
            if values['list_item'][0] == 'その他':
                if not values['other']:
                    sg.popup('その他の項目を入力してください')
                    continue
                choose_item = values['other'] #入力された値
            else:
                choose_item = values['list_item'][0] # 選択された値

        if not is_number(income) or not is_number(expense):
            sg.popup('金額は数字で入力してください')
            continue

        #保存分岐
        if edit_index is not None:
            history_data[edit_index] = [
                entry_calander,
                choose_item,
                entry_content,
                int(income),
                int(expense),
                0
            ]
            sg.popup('更新しました')
            edit_index = None #編集モード終了
        else:
            history_data.append([
                entry_calander,
                choose_item,
                entry_content,
                int(income),
                int(expense),
                0
            ])
            sg.popup('保存しました')

        current_window['text_date'].update(value='')
        current_window['list_item'].update(set_to_index=[])
        current_window['other'].update(value='', disabled=True)
        current_window['input_content'].update(value='')
        current_window['input_income'].update(value='')
        current_window['input_expense'].update(value='')
        current_window['input_net'].update(value='')
    
    
current_window.close()