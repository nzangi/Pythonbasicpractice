# names = []
# subjects = []
# marks = []
#
#
# for i in range(5):
#     name = input(f"Please enter the names of student {i + 1} : ")
#     names.append(name)
#     for j in range(5):
#         subject = input("Enter the names of subject to calculate the sum and average: ")
#         subjects.append(subject)
#         for k in range(5):
#             total = 0
#             mark = int(input("Please  input the marks of each student accordingly to the subject: "))
#             marks.append(mark)
#
names = []
subjects = []
marks = []
averages = []
totals = []

number_of_students = int(input("Please Enter the number of students who you want to calculate their marks: "))
for i in range(number_of_students):
    name = input(f"Please enter the name of student {i+1}: ")
    names.append(name)

    student_subjects = []
    student_marks = []

    for k in range(2):
        subject = input(f"Enter the name of subject  of {name} DONE IN EXAM: ")
        student_subjects.append(subject)
        mark = int(input(f"Please Enter the marks of {name} with respect to {subject}: "))
        student_marks.append(mark)

    subjects.append(student_subjects)
    marks.append(student_marks)
    total = sum(student_marks)
    totals.append(total)
    average = total / len(marks)
    averages.append(average)

for i in range(number_of_students):
    print(names[i]+ ":" + str(subjects[i]) + ":" + str(marks[i])+ str(totals) + ":" + str(averages))
