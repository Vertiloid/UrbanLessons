from time import sleep
from threading import Thread





class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError
        if isinstance(power, int):
            if power == 0:
                raise ZeroDivisionError
            self.power = power
        else:
            raise TypeError

    def get_right_endings(self, n, word):
        correct_endings = {'days': ['день', 'дня', 'дней'], 'warriors': ['воин', 'воина', 'воинов']}
        if n % 10 == 1 and n % 100 != 11:
            p = 0
        elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            p = 1
        else:
            p = 2
        return str(n) + ' ' + correct_endings[word][p]

    def run(self):

        print(f'{self.name}, на нас напали!')
        remainder = 100
        num_of_days = 0
        while remainder:
            """
            if remainder > self.power:
                sleep(1)
            else:
                sleep(remainder / self.power)
            """
            sleep(1)
            num_of_days += 1
            remainder -= self.power
            if remainder < 0:
                remainder = 0
            print(f'{self.name} сражается {self.get_right_endings(num_of_days,"days")} ..., '
                  f'осталось {self.get_right_endings(remainder, "warriors")}.')
        print(f'{self.name} одержал победу спустя {self.get_right_endings(num_of_days, "days")}!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
my_knight = Knight('Sir Gawain', 12)

first_knight.start()
second_knight.start()
my_knight.start()

first_knight.join()
second_knight.join()
my_knight.join()
