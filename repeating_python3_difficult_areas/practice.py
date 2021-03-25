names = []
subjects = []
marks = []
totals = []
averages = []

# subjects = ['MATHS', 'ENGLISH', 'KISWAHILI', 'SCIENCE', 'SOCIAL STUDIES']

number_of_students = int(input("Please enter the TOTAL number of students to be in the list NAMES: "))
for i in range(number_of_students):
    name = input(f"Enter the name of student {i + 1}: ")
    names.append(name)

    # student_subjects = []
    student_marks = []
    subjects = ['MATHS', 'ENGLISH', 'KISWAHILI', 'SCIENCE', 'SOCIAL STUDIES']
    for subject in subjects:
        mark = int(input(f"Please enter the number of MARKS of student {name.upper()} scored in"
                         f" {subject}: "))
        student_marks.append(mark)
    marks.append(student_marks)
    total = sum(student_marks)
    totals.append(total)
    average = total / len(student_marks)
    averages.append(average)
print("NAME    MATHS    ENGLISH   KISWAHILI   SCIENCE   SOCIAL STUDIES  TOTAL  AVERAGE")

output = ""
for i in range(number_of_students):
    output += names[i]+"\t"

    for mark in marks[i]:
        output += str(mark)+"\t\t\t"
    output += str(totals[i])+"\t\t" + str(averages[i])+"\n"

print(output)

# print(names[i]+"\t", str(marks[i][i])+"\t\t\t", str(marks[i][i+1])+"\t\t", str(marks[i][i+2])+"\t\t",
#       str(marks[i][i+3])+"\t\t\t", str(marks[i][i+4])+"\t\t\t",str(totals[i])+"\t\t\t", str(averages[i])+"\t\t\t")

# number_of_subjects = int(input("Please enter NUMBER OF SUBJECTS the student did: "))


#     for k in range(number_of_subjects):
#         subject = input("Please Enter the name of the subject: ")
#         student_subjects.append(subject)
#
#         mark = int(input(f"Please enter the number of MARKS of student {name.upper()} scored in {subject.upper()}: "))
#         student_marks.append(mark)
#
#     subjects.append(student_subjects)
#     marks.append(student_marks)
#     total = sum(student_marks)
#     totals.append(total)
#     average = total / len(student_subjects)
#     averages.append(average)
#
# for i in range(number_of_students):
#     print(names[i] + ":" + str(subjects[i]) + ":" + str(marks[i]) + ":" + str(totals) + ":" + str(averages))
