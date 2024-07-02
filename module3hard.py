def calculate_structure_sum(struc):
    if isinstance(struc, int):
      return struc
    if isinstance(struc, str):
      return len(struc)
    sum = 0
    if any((isinstance(struc, list), isinstance(struc, tuple), isinstance(struc, set))):
      for i in struc:
        sum += calculate_structure_sum(i)
      return sum
    if isinstance(struc, dict):
        for i in struc:
            sum += calculate_structure_sum(i)
            sum += calculate_structure_sum(struc[i])
        return sum


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)