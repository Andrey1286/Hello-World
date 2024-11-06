# Файлы в операционной системе
import os

print('Текущая директория: ', os.getcwd())  # получаем путь к папке, в которой находимся
# if os.path.exists('second'):                # проверка наличия файла/папки
#     os.chdir('second')                      # изменить файл/папку
# else:
#     os.mkdir('second')                      # создать файл/папку
#     os.chdir('second')                      # изменить файл/папку
# print('Текущая директория: ', os.getcwd())  # посмотреть текущее расположение
# print(os.listdir())                         # посмотреть вложенные папки
#
#
#
# os.makedirs(r'Sunday\saturday')             # создаем вложенные папки в текущую директорию
#
# for i in os.walk('.'):                      # '.' - текущая директория. Метод позволяет посмотреть вложенности в директории
#     print(i)

os.chdir(r'C:\Проекты Python\Hello World\module_7')
print('Текущая директория: ', os.getcwd())

print(os.listdir())

file = [f for f in os.listdir() if os.path.isfile(f)]  # переменная для сохранения списка файлов
dirs = [d for d in os.listdir() if os.path.isdir(d)]   # переменная для сохранения списка папок

print(file)

print(dirs)

os.startfile(file[5])  # способ открытия фала

print(os.stat(file[6]))  # получаем информацию о файле

print(os.stat(file[6]).st_size)  # получаем информацию о размере файла

os.system('pip install random2')


