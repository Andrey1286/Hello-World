import threading
import time
from queue import Queue
import random

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None



class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        x = random.randint(3,10)
        time.sleep(x)


class Cafe():
    def __init__(self, tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):  # прибытие гостей
        self.queue.put(self.number)
        for guest in guests:
            if self.quest is None:
            self.queue.get()

            if table.quest is None:


                    print(f'{self.name} сел(-а) за стол номер {}')


    def discuss_guests(self): # обслужить гостей


tables = [Table(number) for number in range(1, 6)]
        # Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
                ]
        # Создание гостей
guests = [Guest(name) for name in guests_names]
        # Заполнение кафе столами
cafe = Cafe(*tables)
        # Приём гостей
cafe.guest_arrival(*guests)
        # Обслуживание гостей
cafe.discuss_guests()