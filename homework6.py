my_dict = {'Название': 'Фланец', 'Шифр': 345123, 'Наличие': 5, 'Место': '9:9-10:10'}
print(my_dict)
print(my_dict.get('Наличие'))
print(my_dict.get('Размер'))
my_dict.update({'Размер': 120, 'Узел': 'Муфта'})
print(my_dict.pop('Место'))
print(my_dict)

my_set = {1, 1.0, '1', 2, 2.0, '2', True, 1, 2, 4}
print(my_set)
my_set.update([3, '3'])
my_set.discard(4)
print(my_set)