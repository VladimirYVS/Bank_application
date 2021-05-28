from tkinter import*
from tkinter import ttk as scroll
import base
import Person


def proofing_int(string):
    try:
        int(string)
    except ValueError:
        return 'Вводите пожалуйста только целые числа'


def proofing_string(string):
    for letter in string:
        try:
            int(letter)
            return 'Вводите пожалуйста только буквы'
        except ValueError:
            pass


def check_account(id_ind):
    get_local_base = DB.get()
    indication = 0
    for item in get_local_base:
        id_ = item.split('|')[0]
        if id_ind in id_.split(':')[1]:
            indication += 1
    return indication


def safe_button(account, sets):
    DB.refresh()
    if check_account(account.account_information['id']) == 0:
        count = 0
        gets = account.get()
        for item in gets:
            for key, value in item.items():
                item[key] = sets[count].get()
                count += 1
        account.safe()
    else:
        record = DB.get()
        for items in range(0, len(record)):
            info = record[items].split("|")

            if account.account_information['id'] == info[0].split(':')[1]:
                del record[items]
                break
        with open('base.txt', 'w') as nw_base:
            nw_base.writelines(record)
        safe_button(account, sets)


def label_fill(count_g, window):
    fill_frame = None
    if count_g == 0:
        fill_frame = LabelFrame(window, text='Заполните данные аккаунта', padx=10, pady=10)

    elif count_g == 1:
        fill_frame = LabelFrame(window, text='Заполните данные клиента', padx=10, pady=10)

    elif count_g == 2:
        fill_frame = LabelFrame(window, text='Заполните место жительства', padx=10, pady=10)

    return fill_frame


def readonly(sets):
    if read_non_read.get() == 'readonly':
        read_non_read.set('normal')
    else:
        read_non_read.set('readonly')

    for ent in sets:
        ent.config(state=read_non_read.get())


def fill_account(window, account_=None):

    if account_ is not None:
        normal_button = Button(window, text='Редактировать', command=lambda: readonly(sets))
        normal_button.place(x=100, y=10)
        read_non_read.set('readonly')
        account = account_

    else:
        account = base.Account()

    btn = Button(window, text='Сохранить', command=lambda: safe_button(account, sets))
    btn.grid(row=0, column=0, sticky='W', padx=10, pady=10)

    count = 1
    count_g = 0
    acc = account.get()
    sets = []

    for item in acc:
        frame = label_fill(count_g, window)
        frame.grid(row=count_g + 1, column=0, padx=10, pady=10, sticky='W')
        for key, value in item.items():

            lbl = Label(frame, text=key, font=("Arial", 12), anchor='w', width=15)
            lbl.grid(row=count, column=0)

            if key == 'id' and value == '-':
                ent = Entry(frame, font=("Arial", 12), width=40)
                account.make()
                ent.insert(0, account.account_information['id'])
                ent.grid(row=count, column=1)
                ent.config(state='readonly')

            elif key == 'id' and value != '-':
                ent = Entry(frame, font=("Arial", 12), width=40)
                ent.insert(0, account.account_information['id'])
                ent.grid(row=count, column=1)
                ent.config(state='readonly')

            elif key in ('RUB', 'USD', 'EUR', 'CYN', 'JPY'):
                ent = Entry(frame, font=("Arial", 12), width=40)
                ent.insert(0, str(value))
                ent.grid(row=count, column=1)
                ent.config(state=read_non_read.get())

            else:
                ent = Entry(frame, font=("Arial", 12), width=40)
                ent.grid(row=count, column=1)
                ent.insert(0, str(value))
                ent.config(state=read_non_read.get())

            sets += [ent]

            count += 1
        count_g += 1


def fill_account_window():
    top = top_lvl()
    fill_account(top)
    top.bind('<Destroy>', refresh_table)


def top_lvl(geometry='550x650'):

    top = Toplevel()
    top.title('ХренФинансБанк')
    top.geometry(geometry)
    photo = PhotoImage(file='ХФБ.png')
    top.iconphoto(False, photo)

    return top


def title_table(window):

    gets = DB.get()
    frame = LabelFrame(window)
    frame.place(x=55, y=50)
    a = base.Account()

    for item in gets:
        a.download(item)

        break

    typical_acc_name = a.get_name()
    typical_acc_acc = a.get_account()
    column = 0
    for key, value in typical_acc_name.items():
        row_str = Label(frame, text=key, font=("Arial", 10), width=20, anchor='w')
        row_str.grid(row=0, column=column)
        column += 1

    for key, value in typical_acc_acc.items():
        if key == 'id':
            continue

        row_str = Label(frame, text=key, font=("Arial", 10), width=10, anchor='w')
        row_str.grid(row=0, column=column)
        column += 1
    del a


def print_base(frame, config='all'):
    for widget in frame.winfo_children():
        widget.destroy()

    if config == 'all' or config == 'Ничего не найдено':
        gets = DB.get()
    else:
        gets = config
    rb_value = StringVar()
    row = 0
    for item in gets:
        a = base.Account()
        a.download(item)

        column = 1
        for key, value in a.get_name().items():

            row_str = Label(frame, text=value, font=("Arial", 10), width=20, anchor='w')
            row_str.grid(row=row, column=column)
            column += 1

        for key, value in a.get_account().items():
            if key == 'id':
                rd = Radiobutton(frame, text='V', value=value, variable=rb_value,
                                 command=lambda: the_change(rb_value), indicatoron=0, width=5)
                rd.grid(row=row, column=0)
                continue

            row_str = Label(frame, text=value, font=("Arial", 10), width=10, anchor='w')
            row_str.grid(row=row, column=column)
            column += 1
        row += 1
    del a


def refresh_table(event):

    DB.refresh()
    print_base(second_frame)


def print_find_base(event):
    if text.get() == '':
        txt = ''
    else:
        txt = text.get()
    char = event.char
    txt += char
    print(txt)
    f_row = DB.find_row(txt)
    print_base(second_frame, f_row)


def the_change(id_):

    row = DB.find_row(id_.get())

    acc = base.Account()
    acc.download(str(row[0]))
    top = top_lvl()
    fill_account(top, acc)


main_window = Tk()

main_window.title('ХренФинансБанк')
main_window.geometry('1400x500')

photo = PhotoImage(file='ХФБ.png')
main_window.iconphoto(False, photo)

# var for checkbutton
read_non_read = StringVar()
read_non_read.set('normal')

# button for create a new account
button = Button(main_window, text='Создать Аккаунт', command=fill_account_window)
button.place(x=5, y=5)

# load database
DB = base.DataBase()
get_base = DB.get()

# download database to window with scrollbar
frame_table = LabelFrame(main_window, text='База данных аккаунтов клиентов')
frame_table.place(x=10, y=75)

my_canvas = Canvas(frame_table, width=1300, height=400)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = scroll.Scrollbar(frame_table, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

second_frame = LabelFrame(my_canvas)
my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

title_table(main_window)
print_base(second_frame)

# refresh button
refresh = Button(main_window, text='Обновить', command=lambda: refresh_table('-'))
refresh.place(x=110, y=5)

# search entry
search_label = Label(main_window, text='Поиск - ', font=('Arial', 12))
search_label.place(x=840, y=5)
text = StringVar()
search_entry = Entry(main_window, width=30, font=('Arial', 12), textvariable=text)
search_entry.place(x=900, y=5)

search_entry.bind('<Key>', print_find_base)

# window mainloop
main_window.mainloop()
