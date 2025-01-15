import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.current_day = 0

    def to_study(self):
        print('Студент вчиться')
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print('Студент заснув на парi')
        self.gladness += 3

    def to_chill(self):
        print('Студент пограв у Brawl Stars')
        self.gladness += 5
        self.progress -= 0.15

    def is_alive(self):
        if self.progress < -0.5:
            print('Студента вiдраховано')
            self.alive = False
        elif self.gladness <= 0:
            print('Студент пiшов у всi тяжкi')
            self.alive = False
        elif self.progress > 5:
            print('Студент перевчився')
            self.alive = False

    def end_of_day(self):
        print(f'Щастя = {self.gladness}')
        print(f'Прогрес = {round(self.progress, 2)}')

    def live(self):
        self.current_day += 1
        day = 'Day ' + str(self.current_day) + ' of ' + self.name + ' life '
        print(f'{day:=^50}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

    def __iter__(self):
        return self

    def __next__(self):
        if not self.alive:
            raise StopIteration
        self.live()
        return self.current_day, self.gladness, self.progress

vasyl = Student(name='Vasyl')

for day_info in vasyl:
    print(day_info)
    if not vasyl.alive:
        break