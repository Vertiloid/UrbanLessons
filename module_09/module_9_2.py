first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(e) for e in first_strings if len(e) > 5]
second_result = [(e_fs, e_ss) for e_fs in first_strings for e_ss in second_strings if len(e_fs) == len(e_ss)]
third_result = {e: len(e) for e in first_strings + second_strings if not len(e) % 2}

print(first_result)
print(second_result)
print(third_result)