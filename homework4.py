my_string = input('Введите произвольную строку: ')
print('Длина введёной строки', len(my_string), 'символов.')
print('Строка в верхнем регистре:', '«' + my_string.upper() + '».')
print('Строка в нижнем регистре:', '«' + my_string.lower() + '».')
print('Строка без пробелов:', '«' + my_string.replace(' ', '') + '».')
print('Первый символ строки — это', '«' + my_string[0] + '».')
print('Последний символ строки — это', '«' + my_string[-1] + '».')
