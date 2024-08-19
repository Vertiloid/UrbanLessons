def custom_write(file_name, strings):
    file = open(file_name, mode='w', encoding='utf-8')
    strings_positions = {}
    n = 1
    for i in strings:
        strings_positions[(n, file.tell())] = i
        file.write(i + '\n')
        n += 1
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)