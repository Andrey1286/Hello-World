#
# sales_data = [
#     {"item": "laptop", "price": 1000, "quantity": 3},
#     {"item": "smartphone", "price": 500, "quantity": 5},
#     {"item": "tablet", "price": 300, "quantity": 4},
#     {"item": "headphones", "price": 100, "quantity": 10},
#     {"item": "monitor", "price": 200, "quantity": 6},
# ]
#
# individual_sales = []  # суммы всех продаж по отдельным товарам
# categorized_sales = {}
# for i in sales_data:
#     key = i['item']
#     value = i["price"] * i['quantity']
#     x = i['price'] * i['quantity']
#     categorized_sales[key] = value
#     individual_sales.append(x)
# print(f'Объемы продаж (список): {individual_sales}')
# print(f'Объемы продаж по категориям: {categorized_sales}')
#
# total_sales = 0
# for k in individual_sales:
#     total_sales += k
# print(f'Общее количество всех продаж: {total_sales}')
#
# top_selling_item = max(categorized_sales, key=categorized_sales.get)
#
# print(f'Название товара с наибольшей выручкой: {top_selling_item}')
#
# q = sorted(categorized_sales.items(), key=lambda x: x[1], reverse=True)
# print(f'Топ 3 товара по продажам: {q[:3]}')


# print(f'Возможные действия в прогремме: 1. Добавить студента '
#       f'2. Узнать среднюю оценку студента '
#       f'3. Вывести всех студентов '
#       f'4. Выйти')
#
# school_performance_data = {'Андрей': [4,5,3], 'Анна': [4], 'Антон': [3]}  # словарь в виде "студент: оценки"
# school_performance_data.keys()  # список студентов
#
# while True:
#     select_action = input('Выберите действие: ')
#     if select_action == '1':
#         student_name = input('Введите имя студента: ')
#         evaluation = input('Введите оценку: ')
#         if student_name in school_performance_data:
#             school_performance_data[student_name].append(int(evaluation))
#         else:
#             school_performance_data[student_name] = [int(evaluation)]
#         print(f'Вы добавили студента "{student_name}"')
#     elif select_action == '2':
#         student_name_1 = input('Введите имя студента: ')
#         if student_name_1 in school_performance_data:
#             list_of_grades = school_performance_data.get(student_name_1)
#             average_estimate = sum(list_of_grades) / len(list_of_grades)  # средняя оценка
#             print(f'Средння оценка студента {student_name_1}: {average_estimate:.2f}')
#         else:
#             print(f'Такого студента нет в списке. Выберите другое действие')
#             continue
#     elif select_action == '3':
#         for key, value in school_performance_data.items():
#             print(f'Успеваемость студента {key}: {value}')
#     elif select_action == '4':
#         print(f'Вы вышли из программы')
#         break
#     else:
#         print(f'Неверное значение. Введите цифру от 1 до 4')
#
# """
# Добавление книги (ввод названия, автора и года).
# Поиск книги по названию.
# Вывод списка всех книг (названия, авторы, годы издания).
# Завершение работы программы
# """
#
# print('Как можно пользоваться программой: 1. Добавить книгу 2. Найти книгу по названию 3. Показать все книги 4. Выйти')
#
# list_of_dictionaries = []
#
# while True:
#     select_an_action = input('Выберите действие (введите цифру от 1 до 4): ')
#     if select_an_action == '1':
#         book_title = input('Введите название книги: ')
#         book_author = input('Введите автора книги: ')
#         year_of_publication = input('Введите год издания: ')
#         list_of_dictionaries.append({'title': book_title, 'author': book_author, 'year': year_of_publication})
#         print('Книга успешно добавлена!')
#     elif select_an_action == '2':
#         book_title_1 = input('Введите название книги: ')
#         found = False
#         for i in list_of_dictionaries:
#             if book_title_1.lower() == i['title'].lower():
#                 print(f"Найдена книга: {i['title']}, автор: {i['author']}, год издания: {i['year']}")
#                 found = True
#                 break
#         if not found:
#             print(f'Книга не найдена')
#     elif select_an_action == '3':
#         number = 0
#         for book in list_of_dictionaries:
#             number +=1
#             print(f"{number}. {book['title']}, автор: {book['author']}, год издания: {book['year']}")
#     elif select_an_action == '4':
#         print(f'Выход из программы')
#         break
#     else:
#         print(f'Нет такого действия. Попробуйте еще раз')
#         continue


