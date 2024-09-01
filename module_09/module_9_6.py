from itertools import combinationss
def all_variants(text):
    for i in range(1, len(text) + 1):
        for j in combinations(text, i):
            yield (''.join(list(j)))


a = all_variants("abc")
for i in a:
    print(i)