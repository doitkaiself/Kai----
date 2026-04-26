import PySimpleGUI as sg
from datetime import datetime
from ui.menu import create_menu_window
from ui.input import create_input_window
from ui.history import create_history_window 
from ui.input import accounting_items
from db.database import history_data
from logic.check import is_number
from ui.print import create_print_window
from calendar import monthrange

edit_index = None #編集モードのインデックス
current_window = create_menu_window()
current_window.bind('<Return>','ENTER')
sg.theme('TealMono')






while True:
    event, values = current_window.read()
    
    if event in (sg.WIN_CLOSED, 'close'):
        break

    elif event == 'ENTER':
        current_window.TKroot.focus_get().tk_focusNext().focus()

    #--------
    #画面遷移
    #--------

    elif event == 'create':
        current_window.close()
        current_window = create_input_window()
        current_window.bind('<Return>','ENTER') #最初に作った入力画面へ

    elif event == 'history':
        current_window.close()
        current_window = create_history_window(history_data) 
        current_window.bind('<Return>','ENTER')#履歴画面へ    

    elif event == 'print':
        current_window.close()
        current_window = create_print_window() #印刷画面へ
    
    elif event == 'back':
        current_window.close()
        current_window = create_menu_window() #戻る
    
    elif event == 'month' and 'day' in current_window.AllKeysDict:
        month = int(values['month'])
        day = int(values['day'])
        max_day = monthrange(datetime.now().year, month)[1]
        
        current_window['day'].update(values=list(range(1, max_day + 1)))
    
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

        month_str, day_str = record[0].replace('日', '').split('月')
        current_window['month'].update(value=int(month_str))
        current_window['day'].update(value=int(day_str))
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
    elif event == 'list_item':
        if values['list_item'] and values['list_item'][0] == 'その他':
            current_window['other'].update(disabled=False)
        else:
            current_window['other'].update(disabled=True)
            current_window['other'].update(value='') #リセット

    #差引金額を計算して表示       
    elif event in ('input_income', 'input_expense'):
            income = values['input_income']
            expense = values['input_expense']
            if is_number(income) and is_number(expense):
                net = int(income) - int(expense)
                current_window['input_net'].update(value=str(net))
            else:
                current_window['input_net'].update('')

    #保存して次へ
    elif event == '保存して次へ':
        
        month = int(values['month'])
        day = int(values['day'])
        calendar_data = f"{month}月{day}日"

        try:
            datetime(datetime.now().year, month, day)  # 年は現在の年を使用
        except ValueError:
            sg.popup('無効な日付です')
            continue

        #キーの内容
        entry_content = values['input_content']
        income = values['input_income']
        expense = values['input_expense']

        #入力内容のバリデーション
        
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
                calendar_data,
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
                calendar_data,
                choose_item,
                entry_content,
                int(income),
                int(expense),
                0
            ])
            sg.popup('保存しました')

        today = datetime.now()
        current_window['month'].update(value=today.month)
        current_window['day'].update(value=today.day)
        current_window['list_item'].update(set_to_index=[])
        current_window['other'].update(value='', disabled=True)
        current_window['input_content'].update(value='')
        current_window['input_income'].update(value='')
        current_window['input_expense'].update(value='')
        current_window['input_net'].update(value='')

    
    
    
current_window.close()