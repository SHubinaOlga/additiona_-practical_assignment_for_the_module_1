grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades_0 = len(grades[0])
grades_1 = len(grades[1])
grades_2 = len(grades[2])
grades_3 = len(grades[3])
grades_4 = len(grades[4])

sum_of_marks_0 = sum(grades[0])
sum_of_marks_1 = sum(grades[1])
sum_of_marks_2 = sum(grades[2])
sum_of_marks_3 = sum(grades[3])
sum_of_marks_4 = sum(grades[4])

average_0 = sum(grades[0])/len(grades[0])
average_1 = sum(grades[1])/len(grades[1])
average_2 = sum(grades[2])/len(grades[2])
average_3 = sum(grades[3])/len(grades[3])
average_4 = sum(grades[4])/len(grades[4])

sorted_students = sorted(students)

grade_book = {sorted_students[0]: average_0, sorted_students[1]: average_1, sorted_students[2]: average_2,sorted_students[3]: average_3,sorted_students[4]: average_4}
print(grade_book)















