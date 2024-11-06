import tkinter             # импортируем библиотеку
import os
from tkinter import filedialog


def file_select ():
    filename = filedialog.askopenfilename(initialdir='/', title='Выберите файл',
                                      filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))
    text['text'] = text['text'] + ' ' + filename
    os.startfile(filename)


window = tkinter.Tk()                                                                                     # создаём окно
window.title('Проводник')                                                              # задам название окна (заголовок)
window.geometry('450x200')                                                                          # задаём размер окна
window.configure(bg='beige')                                                              # задаём общий фон (цвет) окна
window.resizable(False, False)                                                # запрещаем менять размер окна
text = tkinter.Label(window, text='Файл:', height=5, width=65, background='gray', fg='blue')  # задаём имя, высоту, ширину, фон

# если ширину не указывать, она подстраивается автоматически под размер надписи

text.grid(column=1, row=1)                                                        # определяем размещение (колонна, ряд)
button_select = tkinter.Button(window, text='Выбрать файл', height=3, width=65, command=file_select)   # создаём кнопку (имя, высота, ширина)
button_select.grid(column=1, row=3)                                               # определяем размещение (колонна, ряд)
window.mainloop()                                                                     # задаётся, чтобы окно обновлялось