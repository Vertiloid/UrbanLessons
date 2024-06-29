calls = 0
counter_by_name = {'string_info': 0, 'is_contains': 0}


def count_calls(func_name):
    global calls, counter_by_name
    calls += 1
    if func_name not in counter_by_name:
        return
    counter_by_name[func_name] += 1


def string_info(string):
    count_calls('string_info')
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls('is_contains')
    for i in list_to_search:
        if string.lower() in i.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

print(f'функция string_info вызвана {counter_by_name["string_info"]} раз(а)')
print(f'функция is_contains вызванa {counter_by_name["is_contains"]} раз(а)')