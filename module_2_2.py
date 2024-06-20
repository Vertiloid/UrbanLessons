first = input("Введите челое число: ")
second = input("Введите ещё одно цнлое число: ")
third = input("И, пожалуйста, ещё одно целое число: ")
if first == second and second == third :
    rez = 3
elif first == second or second == third or third == first :
    rez = 2
else :
    rez = 0
print(f'Одинаковых чисел: {rez}')
