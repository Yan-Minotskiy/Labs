m = int(input())
student_list = []
for i in range(m):
    n = int(input())
    student_list.append([])
    for j in range(n):
        student_list[i].append(input())
for student in student_list[0]:
    yes_no = True
    for lessons in student_list[1:]:
        if student not in lessons:
            yes_no = False
    if yes_no:
        print(student)
