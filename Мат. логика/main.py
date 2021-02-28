from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter import ttk
import tkinter as tk
import math
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

window = Tk()
window.title("ПОДБОР КНИГ ДЛЯ ЧТЕНИЯ")
window.geometry('800x700')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Побор книг')
tab_control.add(tab2, text='Совет жанра')
tab_control.pack(expand=1, fill='both')
window.resizable(False, False)
main_lbl = Label(tab1, text='Параметры поиска', font='arial 10')
main_lbl.place(x=55, y=5)
c1 = BooleanVar()
c2 = BooleanVar()
c3 = BooleanVar()
c4 = BooleanVar()
c5 = BooleanVar()
c6 = BooleanVar()
slider1 = IntVar()
slider2 = IntVar()
slider3 = IntVar()
slider4 = IntVar()
slider5 = IntVar()
slider6 = IntVar()
chk1 = Checkbutton(tab1, text='Оценка читателей', variable=c1)
chk1.place(x=5, y=35)
scale1 = Scale(tab1, from_=0, to=10, orient=HORIZONTAL, resolution=1, variable=slider1, bg='#4d7198', fg='#ffffff')
scale1.place(x=5, y=60, width=200)
chk2 = Checkbutton(tab1, text='Популярность', variable=c2)
chk2.place(x=5, y=105)
scale2 = Scale(tab1, from_=0, to=10, orient=HORIZONTAL, resolution=1, variable=slider2, bg='#4d7198', fg='#ffffff')
scale2.place(x=5, y=130, width=200)
chk3 = Checkbutton(tab1, text='Размер произведения(стр.)', variable=c3)
chk3.place(x=5, y=175)
scale3 = Scale(tab1, from_=100, to=1679, orient=HORIZONTAL, resolution=1, variable=slider3, bg='#4d7198', fg='#ffffff')
scale3.place(x=5, y=200, width=200)
chk4 = Checkbutton(tab1, text='Интересный сюжет', variable=c4)
chk4.place(x=5, y=245)
scale4 = Scale(tab1, from_=0, to=10, orient=HORIZONTAL, resolution=1, variable=slider4, bg='#4d7198', fg='#ffffff')
scale4.place(x=5, y=270, width=200)
chk5 = Checkbutton(tab1, text='Практическая польза', variable=c5)
chk5.place(x=5, y=315)
scale5 = Scale(tab1, from_=0, to=10, orient=HORIZONTAL, resolution=1, variable=slider5, bg='#4d7198', fg='#ffffff')
scale5.place(x=5, y=340, width=200)
chk6 = Checkbutton(tab1, text='Дата создания (год)', variable=c6)
chk6.place(x=5, y=385)
scale6 = Scale(tab1, from_=1700, to=2019, orient=HORIZONTAL, resolution=1, variable=slider6, bg='#4d7198', fg='#ffffff')
scale6.place(x=5, y=410, width=200)
lbl1 = Label(tab1, text='Жанр')
lbl1.place(x=5, y=455)
combo = Combobox(tab1)
genre = (
    'Любой', 'Биография', 'Детектив', 'Детское', 'Интеллектуальная проза', 'Исторические произведения', 'Классика',
    'Произведения о любви', 'Поэзия', 'Приключения', 'Психология', 'Религия', 'Триллер', 'Учебная литература', 'Фантастика')
combo['values'] = genre
combo.current(0)
combo.place(x=5, y=480, width=200)
lbl3 = Label(tab1, text='Строгость параметров (%)')
lbl3.place(x=5, y=525)
var = StringVar()
var.set('60')
spin = Spinbox(tab1, from_=0, to=100, textvariable=var)
spin.place(x=5, y=550, width=200)
lbl2 = Label(tab1, text='Результаты поика', font='arial 10')
lbl2.place(x=430, y=5)
txt = scrolledtext.ScrolledText(tab1, relief=FLAT)
txt.place(x=230, y=45, width=550, height=550)
txt.insert(INSERT,
           'Добро пожаловать в приложение по подбору книги для чтения!\n'
           'Выберите необходимые параметры и нажмите кнопку "ПОИСК".\n')
file = open('База книг.txt')
books = []
for st in file:
    b = [st[0:st.index('.')]]
    st = st[st.index('.') + 1:]
    b.append(st[0:st.index('.')])
    st = st[st.index('.') + 2:]
    b.append(st.split(' '))
    books.append(b)
txt.configure(state=tk.DISABLED)

def sort_p(item):
    return item[2]


def click():
    txt.configure(state=tk.NORMAL)
    p = [-1000, -1000, -1000, -1000, -1000, -1000]
    pl = [10, 10, 1579, 10, 10, 320]
    if c1.get():
        p[0] = slider1.get()
    if c2.get():
        p[1] = slider2.get()
    if c3.get():
        p[2] = slider3.get()
    if c4.get():
        p[3] = slider4.get()
    if c5.get():
        p[4] = slider5.get()
    if c6.get():
        p[5] = slider6.get()
    g = combo.get()
    n = 0
    for i in range(1, len(genre)):
        if g == genre[i]:
            n = i
            break
    result = []
    if n != 0:
        for book in books:
            k = 0
            a = 0
            for j in range(len(p)):
                if p[j] != -1000:
                    a = (math.fabs(p[j] - int(book[2][j]))) / pl[j] + a
                    k += 1
            if k > 0:
                b = a / k < 0.01 * (100 - int(spin.get())) if True else False
                d = a / k
            else:
                d = 0
                b = True
            if book[2][n + 5] == '1' and b:
                result.append((book[0], book[1], d))
        txt.delete(1.0, END)
        result.sort(key=sort_p)
        for i in result:
            txt.insert(INSERT, i[0] + '. ' + i[1] + '.\n')
        if result == []:
            txt.insert(INSERT, 'По вашему запросу ничего не найдено.\n')
    else:
        for book in books:
            k = 0
            a = 0
            for j in range(len(p)):
                if p[j] != -1000:
                    a += math.fabs(p[j] - int(book[2][j])) / pl[j]
                    k += 1
            if k > 0:
                b = a / k <= 0.01 * (100 - int(spin.get())) if True else False
                d = a / k
            else:
                d = 0
                b = True
            if b:
                result.append((book[0], book[1], d))
        txt.delete(1.0, END)
        if result == []:
            txt.insert(INSERT, 'По вашему запросу ничего не найдено.\n')
        else:
            result.sort(key=sort_p)
            for i in result:
                txt.insert(INSERT, i[0] + '. ' + i[1] + '.\n')
    txt.configure(state=tk.DISABLED)


btn = Button(tab1, text="ПОИСК", command=click, font='arial 20', bg='#4d7198', fg='#ffffff')
btn.place(x=5, y=605, width=790, height=70)
window.mainloop()
