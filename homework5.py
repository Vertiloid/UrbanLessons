immutable_var = (12, 12.0, '12', [12, 12.0, '12'], False)
print (immutable_var)

# immutable_var[0] = 13
# 'tuple' object does not support item assignment
# объект 'кортеж' не поддерживает назначение элементов

mutable_list = [12, 12.0, '12', [12, 12.0, '12'], False]
mutable_list[-1] = True
print(mutable_list)