grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(sorted(students))
avarge_score_0 = sum(grades[0]) / len(grades[0])
avarge_score_1 = sum(grades[1]) / len(grades[1])
avarge_score_2 = sum(grades[2]) / len(grades[2])
avarge_score_3 = sum(grades[3]) / len(grades[3])
avarge_score_4 = sum(grades[4]) / len(grades[4])
student_avarge_score = {students[0]: avarge_score_0, students[1]: avarge_score_1, students[2]: avarge_score_2, students[3]: avarge_score_3, students[4]: avarge_score_4}
print(student_avarge_score)


