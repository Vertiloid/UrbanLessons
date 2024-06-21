def get_password(n):
    result = ''
    for i in range(1, n):
        for j in range((i + 1), n):
            if n % (i + j) == 0:
                result = result + str(i) + str(j)
    return result


for i in range(3, 21):
    print(f'{i} - {get_password(i)}')
