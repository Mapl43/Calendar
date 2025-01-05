import calendar
import datetime
from tkinter import *

days = []
now = datetime.datetime.now()
year = now.year
month = now.month


def fill():
    info_label['text'] = calendar.month_name[month] + ', ' + str(year)
    month_days = calendar.monthrange(year, month)[1]
    if month == 1:
        prew_month_days = calendar.monthrange(year - 1, 12)[1]
    else:
        prew_month_days = calendar.monthrange(year, month - 1)[1]
    week_day = calendar.monthrange(year, month)[0]
    for n in range(month_days):
        days[n + week_day]['text'] = n + 1
        days[n + week_day]['fg'] = 'black'
        if year == now.year and month == now.month and n == now.day:
            days[n + week_day - 1]['background'] = 'green'
        else:
            days[n + week_day]['background'] = 'lightgray'
    for n in range(week_day):
        days[week_day - n - 1]['text'] = prew_month_days - n
        days[week_day - n - 1]['fg'] = 'gray'
        days[week_day - n - 1]['background'] = '#f3f3f3'
    for n in range(6 * 7 - month_days - week_day):
        days[week_day + month_days + n]['text'] = n + 1
        days[week_day + month_days + n]['fg'] = 'gray'
        days[week_day + month_days + n]['background'] = '#f3f3f3'


def prew():
    global month, year
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    fill()


def next():
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1
    fill()


root = Tk()
root.geometry("380x380+650+250")
root.update_idletasks()
root.title("Календарь")
root.iconbitmap(default="icon.ico")
prew_button = Button(root, text='<', command=prew)
prew_button.grid(row=0, column=0, sticky='nsew')
next_button = Button(root, text='>', command=next)
next_button.grid(row=0, column=6, sticky='nsew')
info_label = Label(root, text='0', width=1, height=1,
                   font=('Times New Roman', 16, 'bold'))
info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')

for n in range(7):
    lbl = Label(root, text=calendar.day_abbr[n], width=1, height=1,
                font=('Times New Roman', 10, 'normal'))
    lbl.grid(row=1, column=n, sticky='nsew')
for row in range(6):
    for col in range(7):
        lbl = Label(root, text='0', width=4, height=2,
                    font=('Times New Roman', 16, 'bold'))
        lbl.grid(row=row + 2, column=col, sticky='nsew')
        days.append(lbl)
fill()
root.mainloop()
