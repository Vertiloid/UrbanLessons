grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
stud_sorted_alphabetically = sorted(students)
average_student_grades = dict()
for i in range(len(grades)):
    average = sum(grades[i]) / len(grades[i])
    average_student_grades[stud_sorted_alphabetically[i]] = round(average, 2)
print(average_student_grades)

