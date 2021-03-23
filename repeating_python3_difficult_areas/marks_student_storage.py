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
total = 0
avarage = 0

number_of_students = input("Please enter the number of students you want to calculate their marks: ")
for i in number_of_students:
    name = input(f"Please enter the name of student : ")
    names.append(name)
    for k in range(3):
        subject = input(f"Enter the names of subject to calculate the sum and average of {name}: ")
        subjects.append(subject)
        mark = int(input(f"Please  input the marks of {name} accordingly to the {subject}: "))
        marks.append(mark)
        total = sum(marks)
        avarage = total//len(marks)

for i in number_of_students:
    print(names[i] + ":" + subjects[i] + ":" + marks[i] + total + ":" + avarage)
