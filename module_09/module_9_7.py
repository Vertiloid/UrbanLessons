def is_prime(func):
    def wrapper(*args, **kwargs):
        rez_func = func(*args, **kwargs)
        flag = False
        for i in range(2, rez_func // 2 + 1):
            if not rez_func % i:
                flag = True
                break
        if flag:
            print('Составное')
        else:
            print('Простое')
        return rez_func
    return wrapper

@ is_prime
def sum_three(*args):
    rez = 0
    for i in args:
        rez += i
    return rez


result = sum_three(2, 3, 6)
print(result)
