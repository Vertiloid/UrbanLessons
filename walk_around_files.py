import os
import time

for triple_tuple in os.walk('.'):
    for file in triple_tuple[2]:
        print(f'Обнаружен файл: {file}, Путь: {os.path.join(triple_tuple[0], file)}, '
              f'Размер: {os.path.getsize(file)} байт, '
              f'Время изменения: {time.ctime(os.path.getmtime(file))}, '
              f'Родительская директория: {os.pardir}')
