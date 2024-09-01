first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(e[0]) - len(e[1])) for e in list(zip(first, second)) if len(e[0]) - len(e[1]))
second_result = (len(first[i]) == len (second[i]) for i in range(3))

print(list(first_result))
print(list(second_result))
