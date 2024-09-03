from time import sleep
from datetime import datetime
from threading import Thread

def wite_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


variants_of_count = (10, 30, 200, 100)
args_for_wite_words = [(variants_of_count[j], f'example{j + i * 4 + 1}.txt') for i in range(2) for j in range(4)]

time_start = datetime.now()
for i in range(4):
    wite_words(args_for_wite_words[i][0], args_for_wite_words[i][1])
print(f'Работа потоков заняла {datetime.now() - time_start}')

time_start = datetime.now()
t = []
for i in range(4):
    t.append(Thread(target=wite_words, args=(args_for_wite_words[i + 4])))
    t[i].start()
for i in range(4):
    t[i].join()
print(f'Работа потоков заняла {datetime.now() - time_start}')