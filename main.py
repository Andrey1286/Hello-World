# def print_params(*param):
#     print(param)
#
# print_params(1, 2, 3, 4, 5)
#
# def print_params(*param):
#     print(*param)
#
# print_params(1, 2, 3, 4, 5)

# def params(a, b, c):
#     print(a, b, c)
#
# list_ = [1, 2, 3]
# params(*list_)

# def params(a, b, c):
#     print(a, b, c)
#
# dict_ = {'a': 1, 'b' : 2, 'c' : 3}
# params(**dict_)

# def params(**kwargs):
#     print(kwargs)
#
# dict_ = {'a': 1, 'b' : 2, 'c' : 3}
# params(**dict_)


# a = [True, False, False]
#
# print(any(a))

# a = [1, 0, -2]
#
# print(any(a))

# a = [1, 1, 0]
#
# b = 'Привет'
#
# print(dir(a))
# print(dir(b))

# a = [1, 1, 0]
#
# b = 'Привет'
#
# print(isinstance(a, str))
# print(isinstance(b, str))

# a = [1, 1, 1]
# d = [1, 1, 1]
#
# print(help(a))

# def find_max(list_):
#     max_ = list_[0]
#     for i in list_:
#         if i > max_:
#             max_ = i
#     return max_
#
# list_ = [1, 2, 3, -5, 65]
# a = find_max(list_)
# print(a)
#
# def count_even(list_):
#     counter = 0 # т.е. в списке может быть 0 чётных чисел
#     for i in list_:
#         if i % 2 == 0:
#             counter += 1
#     return counter
#
# print(count_even([1, 3, 40, 20, 35, 256, 4, 2]))


# def unique(list_): # будем создавать уникальный список
#     new_list = []
#     for i in list_:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
#
# print(unique([1, 2, 6, 8, 10, 15, 2, 8, 3]))


def calculate_structure_sum(structure):
    total_sum = 0

    if isinstance(structure, int):
        return structure
    elif isinstance(structure, str):
        return len(structure)
    elif isinstance(structure, list) or isinstance(structure, tuple) or isinstance(structure, set):
        for item in structure:
            total_sum += calculate_structure_sum(item)
    elif isinstance(structure, dict):
        for key, value in structure.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)

    return total_sum


# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
# print(result)  # Должно вывести 99

# def calculate_structure_sum(data):
#     total_sum = 0
#
#     if isinstance(data, int):
#         return data
#     elif isinstance(data, str):
#         return len(data)
#     elif isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
#         for item in data:
#             total_sum += calculate_structure_sum(item)
#     elif isinstance(data, dict):
#         for key, value in data.items():
#             total_sum += calculate_structure_sum(key)
#             total_sum += calculate_structure_sum(value)
#
#     return total_sum
#
# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
# print(result)

import math


# def square(x):
#     d = x ** 2
#     def even(x):
#         d = x * 2
#         if d % 2 == 0:
#             print('Четное число')
#         else:
#             print('Нечетное число')
#     even(x)
#     return d
#
#
# a = 5
# b = square(9)
# print(a)
# print(b)

nums = [5, 3, 2, 1, 6, 4, 7]

# def sorted_bubble(ls):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(ls) -1):
#             if ls[i] > ls[i+1]:
#                 ls[i], ls[i+1] = ls[i+1], ls [i]
#                 swapped = True
#
#
# sorted_bubble(nums)
# print(nums)

# def test_function():
#     def inner_function():
#         print('Я в области видимости функции test_function')
#     return inner_function()
#
# test_function()
# #print(inner_function()) # ошибка - не в области видимости

# class Human: # собственный тип данных (как, например, int, str и другие)
#     def __init__(self): # конструктор классов
#         self.name = 'Den'
#
# den = Human()
# max = Human()
#
# print(den == max) # не равны
# print(den is max) # не одно и то же
# print(id(den), id(max)) # адреса различаются (т.е. каждый объект в классе уникален)
# print(type(den))
# print(den.name, max.name)

# class Human: # собственный тип данных (как, например, int, str и другие)
#      def __init__(self, name): # конструктор классов
#          self.name = name
#
# den = Human('Денис')
# max = Human('Максим')
#
# # print(den == max) # не равны
# # print(den is max) # не одно и то же
# # print(id(den), id(max)) # адреса различаются (т.е. каждый объект в классе уникален)
# # print(type(den))
# print(den.name, max.name)

# class Human:
#     def __init__(self, name, age): # self - указатель на самого себя, на объект
#         self.name = name
#         self.age = age
#         self.say_info()
#         self.birthday()
#
#     def say_info(self):
#         print(f'Привет, меня зовут {self.name}, мне {self.age} года/лет')
#
#     def birthday(self):
#         self.age += 1
#         print(f'Привет, меня зовут {self.name}, у меня сегодня день рождения, мне теперь {self.age} года/лет')
#
# den = Human('Денис', 22)
# max = Human('Максим', 23)
#
# print(den.name, den.age)
# print(max.name, max.age)

# class Database:
#      def __init__(self):
#          self.data = {}
#      def add_user(self, username, password):
#          self.data[username] = password
#
# class User:
#
#      """
#
#      Класс пользователя, содержащий атрибуты: логин, пароль
#
#      """
#
#      def __init__(self, username, password, password_confirm):
#          self.username = username
#
#          if password == password_confirm:
#              self.password = password
#
# print(User.__doc__)
#
# if __name__ == '__main__':
#      database = Database()
#      user = User(input('Введите логин: '), input('Введите пароль: '), input('Введите пароль повторно: '))
#      Database.add_user(user.username, user.password)
#
#      print(user)
#
# print(database.data)

# Атрибуты объекта-экземпляра не нужно описывать — как и переменные,
# они начинают существование в момент первого присваивания


# class Robot:
#
#     def __init__(self):
#         self.name = 'R2D2'
#
#     def hello(self):
#         print('привет мир!')


# robot = Robot()
# robot.temperature = 1
# while robot.temperature < 10:
#     robot.temperature *= 2
# print(robot.temperature)
# del robot.temperature
#
# # Атрибуты сохраняются в пространстве имен каждого объекта - у разных объектов они м.б. разные
#
# robot_2 = Robot()
# robot_2.name = 'Валли'
#
# print(robot.name, robot_2.name)
#
# print(robot, robot_2)
# print(robot == robot_2, robot is robot_2)


# Полезные функции для работы с атрибутами
# hasattr(object, name) - проверка существования
# setattr(object, name, value) - установка
# delattr(object, name) - удаление
# name это строка!

# attr_name = 'model'
# if hasattr(robot, attr_name):
#     print(robot.model)
# else:
#     setattr(robot, attr_name, 'android')
# print(robot.model)
# delattr(robot, attr_name)
#
# # то есть можно устанавливать атрибуты динамически, по именам
# for attr_name in ('weight', 'height', ):
#     setattr(robot, attr_name, 42)
# print(hasattr(robot, 'weight'))
# print(robot.weight)
#
# # getattr(object, name, default=None) - получение атрибута
# print(getattr(robot, 'weight'))
# print(getattr(robot, 'speed', 10))

# class Human:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         print(f'Привет, меня зовут {self.name}')
#
# class Student(Human):
#     def __init__(self, name, place):
#         super().__init__(name)
#         self.place = place
#         super().info()
#         print(f'Я тебя люблю!')
#
# human = Human('Андрей')
# print(human.name)
# student = Student('Максим', 'Урбан')
# print(student.name)

# print(hex(ord('h')))
# print(ord('h'))
# bb = b'\x68'
# print(bb.decode())

from pprint import pprint

# name = 'New2.txt'
# file = open(name, 'w')
# pprint(file.write('Priv, \n Privet'))
#
# file.close()

# from pprint import pprint
#
# name2 = 'New2.txt'
# file = open(name2, 'a')
#
# pprint(file.write('\n Privet, Osen'))
#
# print(file.tell())
#
# file.close()

# name = 'Каша'
# pprint(name, '\nя тебя люблю, Каша')

# print("Hello", end=" ")
# print("World!")

# def buy_a_fur_coat():
#     print('Buy a fur coat!')
#     x = 0
#     while x <10:
#         input_value = input('Ваш ответ: ')
#         if input_value == '':
#             print('Everyone is silent, but you buy a fur coat!')
#         else:
#             print(f'Everyone says: "{input_value}", but you buy a fur coat!')
#         x +=1
#
#
# buy_a_fur_coat()


# def custom_write(file_name, strings):
#     file = open(file_name, 'w', encoding='utf-8')  # Открываем файл для записи с кодировкой utf-8
#     strings_positions = {}  # Словарь для хранения позиций строк
#
#     for i, string in enumerate(strings, 1):  # Перебираем строки с индексом, начиная с 1
#         byte_position = file.tell()  # Получаем текущую позицию в байтах
#         file.write(f'{string}\n')  # Записываем строку в файл с новой строкой
#         strings_positions[(i, byte_position)] = string  # Сохраняем кортеж (номер строки, байт) и строку
#     file.close()  # Закрываем файл
#
#     return strings_positions  # Возвращаем словарь с позициями


# Тестовые данные
# info = [
#     'Text for tell.',
#     'Используйте кодировку utf-8.',
#     'Because there are 2 languages!',
#     'Спасибо!'
# ]
#
# # Вызов функции и вывод результата
# result = custom_write('test.txt', info)
# for elem in result.items():
#     print(elem)

# Файлы в операционной системе
# import os
#
# print('Текущая директория: ', os.getcwd())  # получаем путь к папке, в которой находимся
# if os.path.exists('second'):                # проверка наличия файла/папки
#     os.chdir('second')                      # изменить файл/папку
# else:
#     os.mkdir('second')                      # создать файл/папку
#     os.chdir('second')                      # изменить файл/папку
# print('Текущая директория: ', os.getcwd())  # посмотреть текущее расположение
# print(os.listdir())                         # посмотреть вложенные папки



# class Figure:
#     __sides = []
#     __color = ()
#     sides_count = 0
#     filled = True
#
#     def __init__(self, color: tuple, *sides):
#         self.__color = self.__is_valid_color(color)
#         self.__sides = self.__is_valid_sides(sides)
#
#     def __len__(self):
#         len_ = 0
#         for i in self.get_sides():
#             len_ += i
#         return len_
#
#     def __is_valid_color(self, color: tuple):
#         if len(color) == 3:
#             for i in color:
#                 if i <= 0 or i >= 255:
#                     return False
#             return color
#
#     def set_color(self, *rgb):
#         if (self.__is_valid_color(rgb)):
#             self.__color = rgb
#
#     def get_color(self):
#         return self.__color
#
#     def __is_valid_sides(self, sides):
#         if len(sides) == self.sides_count:
#             return list(sides)
#         elif len(sides) == 1:
#             return [sides[0]] * self.sides_count
#
#     def set_sides(self, *new_sides):
#         if len(new_sides) == self.sides_count:
#             sides_input = []
#             for i in new_sides:
#                 sides_input.append(i)
#             self.__sides = sides_input
#
#     def get_sides(self):
#         return self.__sides
#
#
# class Circle(Figure):
#     sides_count = 1
#
#
# class Triangle(Figure):
#     sides_count = 3
#
#
# class Cube(Figure):
#     sides_count = 12
#
#     def get_volume(self):
#         return self.get_sides()[0] ** 3
#
#
# circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)
#
# # Проверка на изменение цветов:
# circle1.set_color(55, 66, 77)  # Изменится
# print(circle1.get_color())
# cube1.set_color(300, 70, 15)  # Не изменится
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
# print(cube1.get_sides())
# circle1.set_sides(15)  # Изменится
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())

def is_prime(sum_three):
    def wrapper(*args, **kwargs):
        result_1 = sum_three(*args, **kwargs)  # Получаем результат из sum_three

        # Проверяем на числа меньше 2
        if result_1 < 2:
            print('Не простое и не составное')
            return result_1  # Возвращаем результат, если он меньше 2

        # Проверяем делимость числа от 2 до sqrt(result_1)
        for i in range(2, int(result_1 ** 0.5) + 1):
            if result_1 % i == 0:  # Если результат делится на i
                print('Составное')  # Это составное число
                return result_1  # Возвращаем результат

        # Если ни одно число не делит result_1, то оно простое
        print('Простое')
        return result_1  # Возвращаем результат

    return wrapper

@is_prime
def sum_three(a, b, c):
    x = a + b + c  # Складываем три числа
    return x  # Возвращаем сумму

# Пример использования
result = sum_three(2, 3, 6)  # Вызываем функцию sum_three с аргументами 2, 3, 6
print(result)  # Выводим результат сложения